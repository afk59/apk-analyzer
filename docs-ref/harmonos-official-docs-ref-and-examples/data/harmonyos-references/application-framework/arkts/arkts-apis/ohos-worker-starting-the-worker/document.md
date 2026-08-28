# @ohos.worker (Starting the Worker)

The Worker thread is an independent thread running in parallel with the main thread. The thread that creates the Worker thread is referred to as the host thread. The URL file passed in during worker creation is executed in the Worker thread. The Worker thread can process time-consuming operations, but cannot directly operate the UI.

Worker primarily provides a multithreaded runtime environment for applications, allowing them to separate from the host thread during execution. This enables scripts to run in background threads for time-consuming operations, reducing the likelihood of blocking the host thread during computing-intensive or high-latency tasks. A Worker instance will not be proactively destroyed once it is created. It consumes resources to keep running. Therefore, you should call the API to terminate it in a timely manner.

The context environment of the Worker thread is independent of that of the UI main thread. The Worker thread does not support UI operations.

For details about the precautions for using Worker, see [Precautions for Worker](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/worker-introduction).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/-y0J-_7TR5KClWYcmBwK4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7190FA1D50F5BA4A44CFDC828B180EB2252524B49926AA932477FAC871385458)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { worker } from '@kit.ArkTS';

#### Constants

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Description |
| :-- | :-- | :-- | :-- |
| workerPort9+ | [ThreadWorkerGlobalScope](#threadworkerglobalscope9) | Yes | 
Object of the Worker thread used to communicate with the host thread.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| parentPort(deprecated) | [DedicatedWorkerGlobalScope](#dedicatedworkerglobalscopedeprecated) | Yes | 

Object of the Worker thread used to communicate with the host thread.

This property is supported since API version 7 and deprecated since API version 9.

You are advised to use **workerPort9+** instead.

 |

#### WorkerOptions

Provides options that can be set for the Worker instance to create.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | 'classic' | 'module' | No | Yes | 
Mode in which the Worker instance executes the script. The **module** type is not supported yet. The default value is **classic**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| name | string | No | Yes | 

Name of the Worker thread. The default value is **undefined**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| shared | boolean | No | Yes | 

Whether sharing of the Worker instance is enabled. Currently, sharing is not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| priority18+ | [ThreadWorkerPriority](#threadworkerpriority18) | No | Yes | 

Priority of the Worker thread. The default value is **MEDIUM**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ThreadWorkerPriority18+

Enumerates the priorities available for Worker threads. For details about the mappings between priorities and QoS levels, see [QoS Level](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/qos-guidelines#qos-level).

**System capability**: SystemCapability.Utils.Lang

| Name | Value | Description |
| :-- | :-- | :-- |
| HIGH | 0 | 
Applies to user-triggered tasks with visible progress, for example, opening a file. A task completes in seconds. It corresponds to **QOS\_USER\_INITIATED**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| MEDIUM | 1 | 

Applies to tasks that complete in seconds. It is the default value of [ThreadWorkerPriority](#threadworkerpriority18) and corresponds to **QOS\_DEFAULT**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| LOW | 2 | 

Applies to tasks that do not require immediate response, such as download. A task completes in several seconds to several minutes. It corresponds to **QOS\_UTILITY**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| IDLE | 3 | 

Applies to background tasks that are invisible to users, such as data synchronization. A task completes in several minutes or even hours. It corresponds to **QOS\_BACKGROUND**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| DEADLINE20+ | 4 | 

Applies to key tasks that require quick completion, such as page loading. A task completes almost instantly. It corresponds to **QOS\_DEADLINE\_REQUEST**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| VIP20+ | 5 | 

Applies to user interaction tasks such as UI thread and animation rendering. The tasks are instant. It corresponds to **QOS\_USER\_INTERACTIVE**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ThreadWorker9+

Before using the following APIs, you must create a ThreadWorker instance. The ThreadWorker class is inherited from [WorkerEventTarget](#workereventtarget9).

#### \[h2\]Properties

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onexit9+ | (code: number) => void | No | Yes | 
Called when the Worker thread exits. The event handler is executed in the host thread. The **code** value is of the number type, where the value **1** indicates abnormal exit and **0** indicates normal exit. The default value is **undefined**.

**Atomic service API**: This property can be used in atomic services since API version 11.

 |
| onerror9+ | (err: [ErrorEvent](#errorevent)) => void | No | Yes | 

Called when an exception occurs in the synchronous code of the **onmessage** callback function. The handler is executed in the host thread. In the callback function, the **err** type is [ErrorEvent](#errorevent), indicating the received abnormal data. The default value is **undefined**.

**Atomic service API**: This property can be used in atomic services since API version 11.

 |
| onAllErrors18+ | [ErrorCallback](#errorcallback18) | No | Yes | 

Called when an exception occurs within the lifecycle of the Worker thread. The event handler is executed in the host thread.

**Atomic service API**: This property can be used in atomic services since API version 18.

 |
| onmessage9+ | (event: [MessageEvents](#messageevents9)) => void | No | Yes | 

Called when the host thread receives a message sent by the Worker thread through the workerPort.[postMessage](#postmessage9-3) or workerPort.[postMessageWithSharedSendable](#postmessagewithsharedsendable12-1) API. The handler is executed in the host thread. In the callback function, the **event** type is [MessageEvents](#messageevents9), indicating the received message data. The default value is **undefined**.

**Atomic service API**: This property can be used in atomic services since API version 11.

 |
| onmessageerror9+ | (event: [MessageEvents](#messageevents9)) => void | No | Yes | 

Called when the Worker thread receives a message that cannot be serialized. The event handler is executed in the host thread. The **event** type is [MessageEvents](#messageevents9), indicating the received message data. The default value is **undefined**.

**Atomic service API**: This property can be used in atomic services since API version 11.

 |

When using the Worker module, you are advised to register the **onAllErrors** callback in the host thread in API version 18 or later to capture various exceptions that may occur during the lifecycle of the Worker thread. In versions earlier than API version 18, you should register the **onerror** callback. If neither of them is registered, JS crash occurs when the Worker thread is abnormal. Note that the **onerror** callback can only capture synchronous exceptions within the **onmessage** callback. Once an exception is captured, the Worker thread will proceed to the destruction process and cannot be used.

The behavior differences between **onAllErrors** and **onerror** are as follows:

1.  Exception capture range
    
    **onAllErrors** can capture global exceptions generated during the **onmessage** callback, timer callback, and file execution of the Worker thread.
    
    **onerror** can capture only exceptions generated by synchronous methods within the **onmessage** callback of the Worker thread. It cannot capture exceptions from multithreaded callbacks or modularization-related exceptions.
    
2.  Thread status after exception capture
    
    After an exception is captured by **onAllErrors**, the Worker thread remains alive and can continue to be used. This allows you to perform additional operations after an exception is captured, without worrying about the thread being terminated.
    
    Once an exception is captured by **onerror**, the Worker thread enters the destruction process and cannot be used. This means that after **onerror** is triggered, the Worker thread will be terminated, and subsequent operations cannot proceed.
    
3.  Applicable scenarios
    
    **onAllErrors** applies to scenarios where all types of exceptions in the Worker thread need to be captured, especially in complex scenarios where the Worker thread must continue running after an exception occurs.
    
    **onerror** is appropriate for simple scenarios where only synchronous exceptions in the **onmessage** callback need to be captured. Since the thread is destroyed after an exception is captured, it is best used when the Worker thread is not needed afterward.
    
    **onAllErrors** is recommended because it provides more comprehensive exception capture capabilities and does not lead to thread termination.
    

#### \[h2\]constructor9+

constructor(scriptURL: string, options?: WorkerOptions)

A constructor used to create a ThreadWorker instance.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scriptURL | string | Yes | 
URL of the Worker thread file.

For details about the rules, see [Precautions for File URLs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/worker-introduction#precautions-for-file-urls).

 |
| options | [WorkerOptions](#workeroptions) | No | Options that can be set for the Worker instance. If this parameter is left empty, the default value is used. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200003 | Worker initialization failed. |
| 10200007 | The worker file path is invalid. |

**Example**

The following uses the **Index.ets** file in the entry module of the stage model as an example to describe how to load the worker file. For details about how to use the library to load the Worker thread file, see [Precautions for File URLs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/worker-introduction#precautions-for-file-urls).

// Index.ets
import { worker } from '@kit.ArkTS';

// URL of the Worker file: "entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets', {name: "WorkerThread"});

#### \[h2\]postMessage9+

postMessage(message: Object, transfer: ArrayBuffer\[\]): void

Sends a message from the host thread to the Worker thread by transferring object ownership.

**System capability**: SystemCapability.Utils.Lang

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Object | Yes | Data to be sent to the Worker thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| transfer | ArrayBuffer\[\] | Yes | ArrayBuffer instance holding an array of objects for which the ownership is transferred to the Worker thread. After the transfer, the objects are available only in the Worker thread. The array cannot be null. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**Example**

// Worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// Create an object in the Worker thread for communicating with the host thread.
const workerPort = worker.workerPort;

// The Worker thread receives information from the host thread.
workerPort.onmessage = (e: MessageEvents): void => {
  // data carries the information sent by the host thread.
  let data: ArrayBuffer = e.data;
  // Write data to the received buffer.
  const view = new Int8Array(data).fill(3);
  // The Worker thread sends information to the host thread.
  workerPort.postMessage(view);
}

// Trigger a callback when an error occurs in the Worker thread.
workerPort.onerror = (err: ErrorEvent) => {
  console.error("worker.ets onerror" + err.message);
}

// Index.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // Create a Worker instance in the host thread.
            const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
            // The host thread transfers information to the Worker thread.
            const buffer = new ArrayBuffer(8);
            workerInstance.postMessage(buffer, \[buffer\]);

            // The ownership of the buffer is transferred to the Worker thread and is unavailable in the host thread.
            // const view = new Int8Array(buffer).fill(3);

            // The host thread receives information from the Worker thread.
            workerInstance.onmessage = (e: MessageEvents): void => {
              // data carries the information sent by the Worker thread.
              let data: Int8Array = e.data;
              console.info("main thread data is  " + data);
              // Terminate the Worker instance.
              workerInstance.terminate();
            }
            // Call onexit().
            workerInstance.onexit = (code) => {
              console.info("main thread terminate");
            }
            // Listen for Worker errors.
            workerInstance.onAllErrors = (err: ErrorEvent) => {
              console.error("main error message " + err.message);
            }
          })
      }
      .width('100%')
      .height('100%')
    }
  }
}

#### \[h2\]postMessage9+

postMessage(message: Object, options?: PostMessageOptions): void

Sends a message from the host thread to the Worker thread by transferring object ownership or copying data. Pass-by-copy is used to pass [Sendable objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Object | Yes | Data to be sent to the Worker thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| options | [PostMessageOptions](#postmessageoptions) | No | 
If this parameter is specified, the data is sent to the Worker thread through ownership transfer. Such data will become unavailable in the host main thread and only remain accessible within the Worker thread.

If this parameter is not specified, the default value **undefined** is used, and data is transferred to the Worker thread through copying.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**Example**

import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.postMessage("hello world");

let buffer = new ArrayBuffer(8);

// When the options parameter is specified, the ownership of the buffer is transferred to the Worker thread and will no longer be accessible from the host thread.
workerInstance.postMessage(buffer, {transfer: \[buffer\]});

#### \[h2\]postMessageWithSharedSendable12+

postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer\[\]): void

Sends a message from the host thread to the Worker thread. In the message, a [Sendable object](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable) is passed by reference, and a non-Sendable object is passed by copy.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Object | Yes | Data to be sent to the Worker thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). If data needs to be shared, see [Sendable Data Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-data-types). |
| transfer | ArrayBuffer\[\] | No | ArrayBuffer instance holding an array of objects for which the ownership is transferred to the Worker thread. After the transfer, the objects are available only in the Worker thread. The array cannot be null. The default value is an empty array. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**Example**

// Index.ets
// Create a SendableObject instance and pass it to the Worker thread through the host thread.

import { worker } from '@kit.ArkTS';
import { SendableObject } from './sendable';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
let object: SendableObject = new SendableObject();
workerInstance.postMessageWithSharedSendable(object);

// Use the postMessage API to pass Sendable objects by copying the data.
workerInstance.postMessage(object);

// sendable.ets
// Define SendableObject.

@Sendable
export class SendableObject {
  a:number = 45;
}

// The worker file path is entry/src/main/ets/workers/Worker.ets.
// Worker.ets
// Receive and access the data passed from the host thread to the Worker thread.

import { SendableObject } from '../pages/sendable';
import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  let obj: SendableObject = e.data;
  console.info("sendable obj is: " + obj.a);
}

#### \[h2\]on9+

on(type: string, listener: WorkerEventListener): void

Adds an event listener for the Worker instance of the host thread. This API provides the same functionality as [addEventListener9+](#addeventlistener9).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to listen for. |
| listener | [WorkerEventListener](#workereventlistener9) | Yes | Callback to invoke when an event of the specified type occurs. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.on("alert", () => {
    console.info("alert listener callback");
})

// Event listeners added using on can be executed multiple times.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

#### \[h2\]once9+

once(type: string, listener: WorkerEventListener): void

Adds an event listener for the Worker instance of the host thread and removes the listener after it is invoked once.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to listen for. |
| listener | [WorkerEventListener](#workereventlistener9) | Yes | Callback to invoke when an event of the specified type occurs. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.once("alert", () => {
  console.info("alert listener callback");
})

workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

// Event listeners added using once are automatically removed after being executed once and cannot be executed multiple times.
// workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

#### \[h2\]off9+

off(type: string, listener?: WorkerEventListener): void

Removes the event listener of the Worker instance in the host thread. This API provides the same functionality as [removeEventListener9+](#removeeventlistener9).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event for which the event listener is to be removed. |
| listener | [WorkerEventListener](#workereventlistener9) | No | Callback for which the listener is to be removed. If this parameter is not passed, all listeners of the specified type are removed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

const handler1 = () => console.info("Handler 1");
const handler2 = () => console.info("Handler 2");

// Register two listeners.
workerInstance.on("alert", handler1);
workerInstance.on("alert", handler2);

// First trigger: Both listeners are executed.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

// Remove the handler1 listener.
workerInstance.off("alert", handler1);

// Second trigger: Only handler2 is executed.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

// Remove all listeners of the alert type.
workerInstance.off("alert");

#### \[h2\]registerGlobalCallObject11+

registerGlobalCallObject(instanceName: string, globalCallObject: Object): void

Registers an object with the ThreadWorker instance of the host thread. In this way, the methods of the object can be called in the Worker thread through [callGlobalCallObjectMethod](#callglobalcallobjectmethod11).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instanceName | string | Yes | Key used for registration, based on which the registered object is identified during method calling. |
| globalCallObject | Object | Yes | Object to register. The ThreadWorker instance holds a strong reference to the object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
  }
}
let registerObj = new TestObj();
// Register registerObj with the ThreadWorker instance.
workerInstance.registerGlobalCallObject("myObj", registerObj);
workerInstance.postMessage("start worker");

// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  try {
    // The method to call does not carry an input parameter.
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessage", 0) as string;
    console.info("worker:", res) // worker: this is a message from TestObj
  } catch (error) {
    // Exception handling.
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
  try {
    // The method to call carries input parameters.
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessageWithInput", 0, "hello there!") as string;
    console.info("worker:", res); // worker: this is a message from TestObj with input: hello there!
  } catch (error) {
    // Exception handling.
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
}

#### \[h2\]unregisterGlobalCallObject11+

unregisterGlobalCallObject(instanceName?: string): void

Unregisters an object with the ThreadWorker instance of the host thread. This API releases the strong reference between the ThreadWorker instance and the target object. No error is reported if no object is matched.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instanceName | string | No | Key used for registration. If this parameter is left blank, all registered objects registered in the ThreadWorker instance are unregistered. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
  }
}
let registerObj = new TestObj();
workerInstance.registerGlobalCallObject("myObj", registerObj);
// Unregister the object.
workerInstance.unregisterGlobalCallObject("myObj");
// Unregister all objects from the ThreadWorker instance.
// workerInstance.unregisterGlobalCallObject();
workerInstance.postMessage("start worker");

#### \[h2\]terminate9+

terminate(): void

Destroys the Worker thread and stops the Worker thread from receiving messages.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200004 | The Worker instance is not running. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.terminate();

#### \[h2\]addEventListener9+

addEventListener(type: string, listener: WorkerEventListener): void

Adds an event listener for the Worker instance of the host thread. This API provides the same functionality as [on9+](#on9).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to listen for. |
| listener | [WorkerEventListener](#workereventlistener9) | Yes | Callback to invoke when an event of the specified type occurs. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

// Execute the callback of the alert type.
workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

#### \[h2\]removeEventListener9+

removeEventListener(type: string, callback?: WorkerEventListener): void

Removes the event listener of the Worker instance in the host thread. This API provides the same functionality as [off9+](#off9).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event for which the event listener is to be removed. |
| callback | [WorkerEventListener](#workereventlistener9) | No | Callback to invoke when the listener is removed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

workerInstance.removeEventListener("alert");

#### \[h2\]dispatchEvent9+

dispatchEvent(event: Event): boolean

Dispatches an event object to the event system of the Worker thread. The event system automatically triggers the callback functions of all registered listeners for that event type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Event](#event) | Yes | Event to dispatch. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Dispatch result. The value **true** is returned if the dispatch is successful; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", () => {
  console.info("alert listener callback");
})

let result: boolean = workerInstance.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.

console.info("dispatchEvent result is: ", result);

The **dispatchEvent** API can be used together with the **on**, **once**, and **addEventListener** APIs. For details, see [Using dispatchEvent with addEventListener](#using-dispatchevent-with-addeventlistener).

#### \[h2\]removeAllListener9+

removeAllListener(): void

Removes all event listeners of the Worker instance in the host thread.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200004 | Worker instance is not running. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.addEventListener("alert", () => {
    console.info("alert listener callback");
})
workerInstance.removeAllListener();

#### WorkerEventTarget9+

Manages an event listener for the Worker thread.

#### \[h2\]addEventListener9+

addEventListener(type: string, listener: WorkerEventListener): void

Adds an event listener for the Worker instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to listen for. |
| listener | [WorkerEventListener](#workereventlistener9) | Yes | Callback to invoke when an event of the specified type occurs. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200005 | The called API is not supported in the worker thread. |

**Example**

// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  })
};

#### \[h2\]removeEventListener9+

removeEventListener(type: string, callback?: WorkerEventListener): void

Removes the event listener of the Worker instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event for which the event listener is to be removed. |
| callback | [WorkerEventListener](#workereventlistener9) | No | Callback to invoke when the listener is removed. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |

**Example**

// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.removeEventListener("alert");
};

#### \[h2\]dispatchEvent9+

dispatchEvent(event: Event): boolean

Dispatches an event object to the event system of the Worker thread. The event system automatically triggers the callback functions of all registered listeners for that event type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Event](#event) | Yes | Event to dispatch. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Dispatch result. The value **true** is returned if the dispatch is successful; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |

**Example**

// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.dispatchEvent({type: "alert", timeStamp: 0}); // timeStamp is not supported yet.
};

The **dispatchEvent** API can be used together with the **addEventListener** API. For details, see [Using dispatchEvent with addEventListener](#using-dispatchevent-with-addeventlistener).

#### \[h2\]removeAllListener9+

removeAllListener(): void

Removes all event listeners from the Worker instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200004 | The Worker instance is not running. |

**Example**

// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.addEventListener("alert", () => {
    console.info("alert listener callback");
  });

  workerPort.removeAllListener();
};

#### ThreadWorkerGlobalScope9+

Implements communication between the Worker thread and the host thread. The **ThreadWorkerGlobalScope** class inherits from [GlobalScope](#globalscope9).

#### \[h2\]Properties

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onmessage9+ | (this: ThreadWorkerGlobalScope, ev: [MessageEvents](#messageevents9)) => void | No | Yes | 
Called when the Worker thread receives a message sent by the host thread through [postMessage](#postmessage9-1) or [postMessageWithSharedSendable](#postmessagewithsharedsendable12). The event handler is executed in the Worker thread. In the callback function, **this** indicates the caller's [ThreadWorkerGlobalScope](#threadworkerglobalscope9), and the **ev** type is [MessageEvents](#messageevents9), indicating the received message data. The default value is **undefined**.

**Atomic service API**: This property can be used in atomic services since API version 11.

 |
| onmessageerror9+ | (this: ThreadWorkerGlobalScope, ev: [MessageEvents](#messageevents9)) => void | No | Yes | 

Called when the Worker thread receives a message that cannot be deserialized. The event handler is executed in the Worker thread. In the callback function, **this** indicates the caller's [ThreadWorkerGlobalScope](#threadworkerglobalscope9), and the **ev** type is [MessageEvents](#messageevents9), indicating the received message data. The default value is **undefined**.

**Atomic service API**: This property can be used in atomic services since API version 11.

 |

#### \[h2\]postMessage9+

postMessage(messageObject: Object, transfer: ArrayBuffer\[\]): void;

Sends a message from the Worker thread to the host thread by transferring object ownership.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| messageObject | Object | Yes | Data to be sent to the host thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| transfer | ArrayBuffer\[\] | Yes | ArrayBuffer instance holding an array of objects for which the ownership is transferred to the host thread. After the transfer, the objects are available only in the host thread. The array cannot be null. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**Example**

// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    console.info("receive data from worker.ets");
}

// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    let buffer = new ArrayBuffer(8);
    workerPort.postMessage(buffer, \[buffer\]);
}

#### \[h2\]postMessage9+

postMessage(messageObject: Object, options?: PostMessageOptions): void

Sends a message from the Worker thread to the host thread by transferring object ownership or copying data. Pass-by-copy is used to pass [Sendable objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| messageObject | Object | Yes | Data to be sent to the host thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| options | [PostMessageOptions](#postmessageoptions) | No | 
If this parameter is specified, it functions the same as **ArrayBuffer\[\]**. Specifically, the ownership of the objects in the array is transferred to the host thread and becomes unavailable in the Worker thread. The objects are available only in the host thread.

If this parameter is not specified, the default value **undefined** is used, and information is transferred to the host thread by copying data.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**Example**

// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    console.info("receive data from worker.ets");
}

// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    workerPort.postMessage("receive data from main thread");
}

#### \[h2\]postMessageWithSharedSendable12+

postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer\[\]): void

Sends a message from the Worker thread to the host thread. In the message, a [Sendable object](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable) is passed by reference, and a non-Sendable object is passed by copy.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Object | Yes | Data to be sent to the host thread. The data object must be sequenceable or sendable. For details about the supported sequenceable types, see [Sequenceable Data Types](#sequenceable-data-types). For details about the supported sendable types, see [Sendable Data Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-data-types). |
| transfer | ArrayBuffer\[\] | No | ArrayBuffer instance holding an array of objects for which the ownership is transferred to the host thread. After the transfer, the objects are available only in the host thread. The array cannot be null. The default value is an empty array. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | The Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |

**Example**

// The worker file path is entry/src/main/ets/workers/Worker.ets.
// Worker.ets
// Create a SendableObject instance and pass it to the host thread through the Worker thread.

import { SendableObject } from '../pages/sendable';
import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  let object: SendableObject = new SendableObject();
  workerPort.postMessageWithSharedSendable(object);
}

// sendable.ets
// Define SendableObject.

@Sendable
export class SendableObject {
  a:number = 45;
}

// Index.ets
// Receive the data passed from the Worker thread to the host thread and access its properties.

import { worker, MessageEvents } from '@kit.ArkTS';
import { SendableObject } from './sendable';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
workerInstance.postMessage(1);
workerInstance.onmessage = (e: MessageEvents) => {
  let obj: SendableObject = e.data;
  console.info("sendable index obj is: " + obj.a);
}

#### \[h2\]callGlobalCallObjectMethod11+

callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object\[\]): Object

Calls a method of an object registered with the host thread. This API is called by the Worker thread. The invoking is synchronous for the Worker thread and asynchronous for the host thread. The return value is passed by copy.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instanceName | string | Yes | Key used for registration. It is used to search for the object in the host thread. |
| methodName | string | Yes | Name of the method to call. This method cannot be modified by async or generator, or return results asynchronously by using the asynchronous mechanism at the bottom layer. Otherwise, an exception is thrown. |
| timeout | number | Yes | 
Maximum waiting time from the time when the Worker thread initiates the call to the time when the target method is executed in the main thread, in milliseconds. The value is an integer ranging from 1 to 5000. The value **0** means that the 5000 ms duration is used.

In versions earlier than API version 21, the maximum waiting time is limited by this parameter in debug mode.

Since API version 21, the maximum waiting time is not limited by this parameter in debug mode.

 |
| args | Object\[\] | No | Array of parameters in the method. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | Return value of the method in the host thread. The return value must be serializable. For details, see [Sequenceable Data Types](#sequenceable-data-types). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200006 | An exception occurred during serialization. |
| 10200019 | The globalCallObject is not registered. |
| 10200020 | The method to be called is not callable or is an async method or a generator. |
| 10200021 | The global call exceeds the timeout. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
class TestObj {
  private message : string = "this is a message from TestObj";
  public getMessage() : string {
    return this.message;
  }
  public getMessageWithInput(str : string) : string {
    return this.message + " with input: " + str;
  }
}
let registerObj = new TestObj();
// Register registerObj with the ThreadWorker instance.
workerInstance.registerGlobalCallObject("myObj", registerObj);
workerInstance.postMessage("start worker");
// Call the following method when the component lifecycle ends:
// workerInstance.unregisterGlobalCallObject("myObj");

// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  try {
    // The method to call does not carry an input parameter.
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessage", 0) as string;
    console.info("worker:", res); // worker: this is a message from TestObj
  } catch (error) {
    // Exception handling.
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
  try {
    // The method to call carries input parameters.
    let res : string = workerPort.callGlobalCallObjectMethod("myObj", "getMessageWithInput", 0, "hello there!") as string;
    console.info("worker:", res); // worker: this is a message from TestObj with input: hello there!
  } catch (error) {
    // Exception handling.
    console.error("worker: error code is " + error.code + " error message is " + error.message);
  }
}

#### \[h2\]close9+

close(): void

Terminates the Worker thread to stop it from receiving messages.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200004 | The Worker instance is not running. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");

// worker.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
    workerPort.close();
}

#### WorkerEventListener9+

Implements event listening.

#### \[h2\](event: Event)9+

(event: Event): void | Promise<void>

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Event](#event) | Yes | Event class for the callback to invoke. |

**Return value**

| Type | Description |
| :-- | :-- |
| void | Promise<void> | Returns no value or returns a **Promise**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200004 | Worker instance is not running. |
| 10200005 | The invoked API is not supported in workers. |

**Example**

// Index.ets
import { worker, Event } from "@kit.ArkTS"

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

workerInstance.addEventListener("alert", (event: Event) => {
  console.info("event type is: ", JSON.stringify(event.type));
});

const eventToDispatch : Event = { type: "alert", timeStamp: 0 }; // timeStamp is not supported yet.
workerInstance.dispatchEvent(eventToDispatch);

#### GlobalScope9+

Implements the running environment of the Worker thread. The **GlobalScope** class inherits from [WorkerEventTarget](#workereventtarget9).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | Worker instance specified when there is a new Worker instance. |
| self | [GlobalScope](#globalscope9) & typeof globalThis | Yes | No | GlobalScope itself. |
| onerror | (ev: [ErrorEvent](#errorevent)) => void | No | Yes | Callback function invoked when an exception occurs during Worker execution. It is executed in the Worker thread. **ev** indicates the exception data received. The default value is **undefined**. |

#### MessageEvents9+

Holds the data transferred between Worker threads. The class inherits from [Event](#event).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | any | Yes | No | Data transferred between threads. |

#### MessageType

type MessageType = 'message' | 'messageerror'

Defines the message type. Reserved data type, which is not implemented yet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Type | Description |
| :-- | :-- |
| 'message' | The message type is message, fixed at **'message'**. |
| 'messageerror' | The message type is messageerror, fixed at **'messageerror'**. |

#### ErrorCallback18+

type ErrorCallback = (err: ErrorEvent) => void

Defines an error callback.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| err | ErrorEvent | Yes | Error event class, which indicates the exception information that occurs during Worker execution. |

#### Worker(deprecated)

Before using the following APIs, you must create a Worker instance. The **Worker** class inherits from [EventTarget](#eventtargetdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/fK-JAJfWSfilx4On585Nkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=559D57D129D480833BA6AFB42456E40E7D9629A68D4F85B05A7BFA54B6A34B4F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker9+](#threadworker9) instead.

#### \[h2\]Properties

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onexit(deprecated) | (code: number) => void | No | Yes | 
Called when the Worker thread exits. The event handler is executed in the host thread. In the callback function, the **code** value is of the number type, where the value **1** indicates abnormal exit and **0** indicates normal exit. The default value is **undefined**.

**Note**: This property is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.onexit](#properties-1) instead.

 |
| onerror(deprecated) | (err: [ErrorEvent](#errorevent)) => void | No | Yes | 

Called when an exception occurs during worker execution. The event handler is executed in the host thread. In the callback function, the **err** type is [ErrorEvent](#errorevent), indicating the received abnormal data. The default value is **undefined**.

**Note**: This property is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.onerror](#properties-1) instead.

 |
| onmessage(deprecated) | (event: [MessageEvent](#messageeventt)) => void | No | Yes | 

Called when the host thread receives a message sent by the Worker thread through **workerPort.postMessage**. The event handler is executed in the host thread. In the callback function, the **event** type is [MessageEvent](#messageeventt), indicating the received message data. The default value is **undefined**.

**Note**: This property is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.onmessage](#properties-1) instead.

 |
| onmessageerror(deprecated) | (event: [MessageEvent](#messageeventt)) => void | No | Yes | 

Called when the Worker thread receives a message that cannot be serialized. The event handler is executed in the host thread. In the callback function, the **event** type is [MessageEvent](#messageeventt), indicating the received message data. The default value is **undefined**.

**Note**: This property is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.onmessageerror](#properties-1) instead.

 |

#### \[h2\]constructor(deprecated)

constructor(scriptURL: string, options?: WorkerOptions)

A constructor used to create a Worker instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/NjSLOTP-Sf-WxEtBJw-ISg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2534296027097DFF7518F58B993A95272192B60B7D3B8C59DDC18F3F3115349A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.constructor9+](#constructor9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scriptURL | string | Yes | URL of the Worker thread file. For details about the rules, see [Precautions for File URLs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/worker-introduction#precautions-for-file-urls). |
| options | [WorkerOptions](#workeroptions) | No | Options that can be set for the Worker instance. |

**Example**

The following uses the **Index.ets** file in the entry module of the stage model as an example to describe how to load the worker file. For details about how to use the library to load the Worker thread file, see [Precautions for File URLs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/worker-introduction#precautions-for-file-urls).

// Index.ets
import { worker } from '@kit.ArkTS';

// URL of the Worker file: "entry/src/main/ets/workers/worker.ets"
const workerInstance = new worker.Worker('entry/ets/workers/worker.ets', {name: "WorkerThread"});

#### \[h2\]postMessage(deprecated)

postMessage(message: Object, transfer: ArrayBuffer\[\]): void

Sends a message from the host thread to the Worker thread by transferring object ownership.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/QXk19saETHiygIiKr7z7_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51348ED3E1C7D88222ABD31E7014E07D968BC91D55D864D982D01C4710C56836)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.postMessage9+](#postmessage9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Object | Yes | Data to be sent to the Worker thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| transfer | ArrayBuffer\[\] | Yes | ArrayBuffer instance holding an array of objects for which the ownership is transferred to the Worker thread. After the transfer, the objects are available only in the Worker thread. The array cannot be null. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");

let buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, \[buffer\]);

#### \[h2\]postMessage(deprecated)

postMessage(message: Object, options?: PostMessageOptions): void

Sends a message from the host thread to the Worker thread by transferring object ownership or copying data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/PEP0MJySTdm4o8sRE-U2pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F00C61F6C5827CFF9DE4D4E538B455C8638BC84C47FCC1E1AFE3D022ED8E20B4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.postMessage9+](#postmessage9-1) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Object | Yes | Data to be sent to the Worker thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| options | [PostMessageOptions](#postmessageoptions) | No | 
If this parameter is specified, it functions the same as **ArrayBuffer\[\]**. Specifically, the ownership of the objects in the array is transferred to the Worker thread and becomes unavailable in the host thread. The objects are available only in the Worker thread.

If this parameter is not specified, the default value **undefined** is used, and information is transferred to the Worker thread by copying data.

 |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");

workerInstance.postMessage("hello world");

let buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, \[buffer\]);

#### \[h2\]on(deprecated)

on(type: string, listener: EventListener): void

Adds an event listener for the Worker thread. This API provides the same functionality as [addEventListener(deprecated)](#addeventlistenerdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/oVIU0VP8SJyxLg3e9cn7Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F403B9B3870EDB89DCA8951491A4DDAF678F080F3F46CBAAAA92E439A01B7D5)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.on9+](#on9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to listen for. |
| listener | [EventListener](#eventlistenerdeprecated) | Yes | Callback to invoke when an event of the specified type occurs. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.on("alert", () => {
    console.info("alert listener callback");
})

#### \[h2\]once(deprecated)

once(type: string, listener: EventListener): void

Adds an event listener for the Worker thread and removes the event listener after it is invoked once.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/4e4ZJuNNRyWUmosJ9zBTfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2305FB4D2D8FAFBB4C6A63E8022F2375AB9D36D75FF736FBE991257DC7EC1ED)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.once9+](#once9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to listen for. |
| listener | [EventListener](#eventlistenerdeprecated) | Yes | Callback to invoke when an event of the specified type occurs. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.once("alert", () => {
    console.info("alert listener callback");
})

#### \[h2\]off(deprecated)

off(type: string, listener?: EventListener): void

Removes an event listener for the Worker thread. This API provides the same functionality as [removeEventListener(deprecated)](#removeeventlistenerdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/WH2nYAFIQteODL-fO1xmNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10CC8CD30CB7623B1E82E3E45F797EB31FF0976F9B53FA9C06603F21972FB31F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.off9+](#off9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event for which the event listener is to be removed. |
| listener | [EventListener](#eventlistenerdeprecated) | No | Callback to invoke when the listener is removed. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
// Use on, once, or addEventListener to add a listener for the "alert" event, and use off to remove the listener.
workerInstance.off("alert");

#### \[h2\]terminate(deprecated)

terminate(): void

Terminates the Worker thread to stop it from receiving messages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/hnHY_-c5R-OCmTSYraUMXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBFEA4C6E0F119127B354BCD0E1EC2D42929B1D3C6DDEB3BA0289A495836E417)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorker.terminate9+](#terminate9) instead.

**System capability**: SystemCapability.Utils.Lang

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.terminate();

#### EventTarget(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/0ffIn66bS42a7nsMGWS44w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AEFF5F214F548430B50199E153D27E746970BA1F7D57ABF3526224D010787C2)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [WorkerEventTarget9+](#workereventtarget9) instead.

#### \[h2\]addEventListener(deprecated)

addEventListener(type: string, listener: EventListener): void

Adds an event listener for the Worker thread. This API provides the same functionality as [on(deprecated)](#ondeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/uGBbUlIwTt-W4r9h_CEmVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=510FD8530310B95F3D31A829E5B6D8B4170CBBBC818EEA193AAE910801484964)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [addEventListener9+](#addeventlistener9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to listen for. |
| listener | [EventListener](#eventlistenerdeprecated) | Yes | Callback function invoked upon event triggering. |

**Example**

// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})

#### \[h2\]removeEventListener(deprecated)

removeEventListener(type: string, callback?: EventListener): void

Removes an event listener for the Worker thread. This API provides the same functionality as [off(deprecated)](#offdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/nIvA_70xTAONSmZPjbdueA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8F02DA88F68DD866D77E08466B038A8A39A77F023849E7110DF7C4A33F22B67)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [removeEventListener9+](#removeeventlistener9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to be removed. |
| callback | [EventListener](#eventlistenerdeprecated) | No | Callback to invoke when the listener is removed. |

**Example**

// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", () => {
  console.info("alert listener callback");
})

workerPort.removeEventListener('alert');

#### \[h2\]dispatchEvent(deprecated)

dispatchEvent(event: Event): boolean

Dispatches the event defined for the Worker thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/1oMrrhvCQjmCDQnGjxgWMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8A4355ACE96A15711CBD8E08EC9D4353913C3096FBED86F0B90D79C2199D9D3)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [dispatchEvent9+](#dispatchevent9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [Event](#event) | Yes | Event to dispatch. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Dispatch result. The value **true** is returned if the dispatch is successful; otherwise, **false** is returned. |

**Example**

// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert\_add", ()=>{
  console.info("alert listener callback");
})

workerPort.dispatchEvent({type: 'alert\_add', timeStamp: 0}); // timeStamp is not supported yet.

The **dispatchEvent** API can be used together with the **addEventListener** API. The sample code is as follows:

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (): void => {
    console.info("receive data from worker.ets");
}

// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert", ()=>{
  console.info("alert listener callback");
})

workerPort.onmessage = (event: MessageEvents) => {
  workerPort.dispatchEvent({type:"alert", timeStamp:0}); // timeStamp is not supported yet.
}

#### \[h2\]removeAllListener(deprecated)

removeAllListener(): void

Removes all event listeners for the Worker thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/_0fofX4sRhai_c93rgStCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDC057BECC263C3F3DBB4C194E6750F24233414E7DBC6953D3A740F9B0F93590)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [removeAllListener9+](#removealllistener9) instead.

**System capability**: SystemCapability.Utils.Lang

**Example**

// worker.ets
import { DedicatedWorkerGlobalScope, ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.addEventListener("alert\_add", ()=>{
  console.info("alert listener callback");
})

workerPort.removeAllListener();

#### DedicatedWorkerGlobalScope(deprecated)

Implements communication between the Worker thread and the host thread. This class inherits from [WorkerGlobalScope](#workerglobalscopedeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/mhjNbk67QCuCHzSVp_zhZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52EBC25C214B7CD119E6A7E2B9806BC3A4F30FACE8C04574668B64C30106205A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorkerGlobalScope9+](#threadworkerglobalscope9) instead.

#### \[h2\]Properties

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| onmessage(deprecated) | (this: DedicatedWorkerGlobalScope, ev: [MessageEvent](#messageeventt)) => void | No | Yes | 
Called when the Worker thread receives a message sent by the host thread through **postMessage**. The event handler is executed in the Worker thread. In the callback function, **this** indicates the caller's [DedicatedWorkerGlobalScope](#dedicatedworkerglobalscopedeprecated), and the **ev** type is [MessageEvent](#messageeventt), indicating the received message data. The default value is **undefined**.

**Note**: This property is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorkerGlobalScope.onmessage](#properties-2) instead.

 |
| onmessageerror(deprecated) | (this: DedicatedWorkerGlobalScope, ev: [MessageEvent](#messageeventt)) => void | No | Yes | 

Called when the Worker thread receives a message that cannot be deserialized. The event handler is executed in the Worker thread. In the callback function, **this** indicates the caller's [DedicatedWorkerGlobalScope](#dedicatedworkerglobalscopedeprecated), and the **ev** type is [MessageEvent](#messageeventt), indicating the received message data. This property is supported since API version 7. The default value is **undefined**.

**Note**: This property is deprecated since API version 9. You are advised to use [ThreadWorkerGlobalScope.onmessageerror](#properties-2) instead.

 |

#### \[h2\]postMessage(deprecated)

postMessage(messageObject: Object, transfer: Transferable\[\]): void

Sends a message from the Worker thread to the host thread by transferring object ownership.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/BxmtwySRTeyQiyqiZ21zrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A980F989DC3C05680837372719AD3BF3A89CCB50ABB60EE86740358946E6FEA2)

This API is deprecated since API version 9. You are advised to use [ThreadWorkerGlobalScope9+.postMessage9+](#postmessage9-2).

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| messageObject | Object | Yes | Data to be sent to the host thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| transfer | Transferable\[\] | Yes | Currently, this parameter is not supported. |

#### \[h2\]postMessage(deprecated)

postMessage(messageObject: Object, transfer: ArrayBuffer\[\]): void

Sends a message from the Worker thread to the host thread by transferring object ownership.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/QQ6ltXWiT_Ovt55kGEhUig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D721B6BB1F0947025C5B7D951207F8224892EFDF716025657CD6C9C50E74506)

The **postMessage** API is supported since API version 9 and deprecated since API version 9. You are advised to use [ThreadWorkerGlobalScope9+.postMessage9+](#postmessage9-2) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| messageObject | Object | Yes | Data to be sent to the host thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| transfer | ArrayBuffer\[\] | Yes | ArrayBuffer instance holding an array of objects for which the ownership is transferred to the host thread. After the transfer, the objects are available only in the host thread. The array cannot be null. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (e: MessageEvents): void => {
    // let data = e.data;
    console.info("receive data from worker.ets");
}

// worker.ets
import { DedicatedWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: DedicatedWorkerGlobalScope = worker.parentPort;

workerPort.onmessage = (): void => {
    // let data = e.data;
    let buffer = new ArrayBuffer(5)
    workerPort.postMessage(buffer, \[buffer\]);
}

#### \[h2\]postMessage(deprecated)

postMessage(messageObject: Object, options?: PostMessageOptions): void

Sends a message from the Worker thread to the host thread by transferring object ownership or copying data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/-xcbChXKQ_-64gGujUMXYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96033E60F13B76762A91604CA360BC074B6AA4556DB94F2298FD56EE93F3BED8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorkerGlobalScope9+.postMessage9+](#postmessage9-3).

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| messageObject | Object | Yes | Data to be sent to the host thread. The data object must be sequenceable. For details about the supported parameter types, see [Sequenceable Data Types](#sequenceable-data-types). |
| options | [PostMessageOptions](#postmessageoptions) | No | 
If this parameter is specified, it functions the same as **ArrayBuffer\[\]**. Specifically, the ownership of the objects in the array is transferred to the host thread and becomes unavailable in the Worker thread. The objects are available only in the host thread.

If this parameter is not specified, the default value **undefined** is used, and information is transferred to the host thread by copying data.

 |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");
workerInstance.onmessage = (): void => {
    console.info("receive data from worker.ets");
}

// worker.ets
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const parentPort = worker.parentPort;
parentPort.onmessage = (e: MessageEvents) => {
  parentPort.postMessage("receive data from main thread");
}

#### \[h2\]close(deprecated)

close(): void

Terminates the Worker thread to stop it from receiving messages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/2dMYfMmCTW2mE5wWxWZvrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FB05BD09790212F4239016F1F165BC4727166E5E19D4033775DA88788654229)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [ThreadWorkerGlobalScope9+.close9+](#close9).

**System capability**: SystemCapability.Utils.Lang

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.postMessage("hello world");

// worker.ets
import { worker } from '@kit.ArkTS';

const parentPort = worker.parentPort;
parentPort.onmessage = (): void => {
    parentPort.close()
}

#### PostMessageOptions

Defines the object for which the ownership is to be transferred during data transfer. The object must be an ArrayBuffer instance. After the ownership is transferred, the object becomes unavailable in the sender and can be used only in the receiver.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| transfer | Object\[\] | No | Yes | **ArrayBuffer** array used to transfer the ownership. The array cannot be **null**. The default value is **undefined**. |

#### Event

Defines the event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | string | Yes | No | Type of the event. |
| timeStamp | number | Yes | No | Timestamp (accurate to millisecond) when the event is created. This parameter is not supported yet. |

#### EventListener(deprecated)

Defines an event listener.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/dJ4viIA-SEia-ghxOeWfQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7E7CE6CFA21F2356DDA749DA04616B5F4B3244D231B64C86D5A7D61E3514CB2)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [WorkerEventListener9+](#workereventlistener9) instead.

#### \[h2\](evt: Event)(deprecated)

(evt: Event): void | Promise<void>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/8_WTVONyQ7e_NuyZ2E9-SA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=353EF523F560A9F753D603822A1BB73EB7FB85B00329A76DC57A93A8B3559866)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [(event:Event)](#event-event9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| evt | [Event](#event) | Yes | Event class for the callback to invoke. |

**Return value**

| Type | Description |
| :-- | :-- |
| void | Promise<void> | Returns no value or returns a **Promise**. |

**Example**

// Index.ets
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.Worker("entry/ets/workers/worker.ets");
workerInstance.addEventListener("alert", ()=>{
    console.info("alert listener callback");
})

#### ErrorEvent

Provides detailed information about the exception that occurs during worker execution. This class inherits from [Event](#event).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| message | string | Yes | No | Information about the exception. |
| filename | string | Yes | No | File where the exception is located. |
| lineno | number | Yes | No | Serial number of the line where the exception is located. |
| colno | number | Yes | No | Serial number of the column where the exception is located. |
| error | Object | Yes | No | Type of the exception. |

#### MessageEvent<T>

Holds the data transferred between Worker threads. The class inherits from [Event](#event).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | T | Yes | No | Data transferred between threads. |

#### WorkerGlobalScope(deprecated)

Implements the running environment of the Worker thread. The **WorkerGlobalScope** class inherits from [EventTarget](#eventtargetdeprecated).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/UhaLvzSpS36JjUjnk7JZsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17C684CCCEEAC09A5FB6DAC0868C6AA44600AEFEDEC93E86A6CBFB611ADCCF76)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [GlobalScope9+](#globalscope9) instead.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | Worker instance specified when there is a new Worker instance. |
| self | [WorkerGlobalScope](#workerglobalscopedeprecated) & typeof globalThis | Yes | No | WorkerGlobalScope. |
| onerror | (ev: [ErrorEvent](#errorevent)) => void | No | Yes | Callback function invoked when an exception occurs during Worker execution. It is executed in the Worker thread. **ev** indicates the exception data received. The default value is **undefined**. |

#### More Information

## Sequenceable Data Types

The following object types are supported: basic types except Symbol, Date, String, RegExp, Array, Map, Set, Object (simple objects only, for example, objects created using **{}** or **new Object**), ArrayBuffer, and TypedArray. (Note that only properties can be transferred for common objects. Prototypes and methods cannot be transferred.)

Exception: When an object created through a custom class is passed, no serialization error occurs. However, the properties (such as Function) of the custom class cannot be passed through serialization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/V4KnwL5AQW2zSsMhkEJs2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BA20617D6EE2C1202A1E76D9D8ABDA8D3F5F6DBBC3DB7B310A18E55C8AE3AEA)

An FA project of API version 9 is used as an example.

// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("workers/worker.ets");
workerInstance.postMessage("message from main thread to worker");
workerInstance.onmessage = (d: MessageEvents): void => {
  // When the Worker thread passes obj2, data contains obj2, excluding the Init or SetName method.
  let data: string  = d.data;
}

// worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

const workerPort = worker.workerPort;
class MyModel {
    name = "undefined";
    Init() {
        this.name = "MyModel";
    }
}
workerPort.onmessage = (d: MessageEvents): void => {
  console.info("worker.ets onmessage");
  let data: string = d.data;
  let func1 = () => {
    console.info("post message is function");
  }
  // workerPort.postMessage(func1); A serialization error occurs when passing func1.
  let obj2 = new MyModel();
  workerPort.postMessage(obj2);     // No serialization error occurs when passing obj2, but the functions in obj2 are lost.
}
workerPort.onmessageerror = () => {
    console.error("worker.ets onmessageerror");
}
workerPort.onerror = (err: ErrorEvent) => {
    console.error("worker.ets onerror" + err.message);
}

## Memory Model

The Worker thread is implemented based on the actor model. In the Worker interaction process, the host thread can create multiple Worker threads. The running environments of Worker threads are isolated from each other. Objects are transferred through serialization, reference passing, or ownership transfer. After the Worker threads complete computing tasks, the results are returned to the host thread.

Each actor concurrently processes tasks of the host thread. For each actor, there is a message queue and a single-thread execution module. The message queue receives requests from the host thread and other actors; the single-thread execution module serially processes requests, sends requests to other actors, and creates new actors. These isolated actors use the asynchronous mode and can run concurrently.

#### Sample Code

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/kt9WJBpaRSy-udYu7h-v_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3F8405BCDAF08069591ED713642D9FC2C834D89C7EC208F4A6F9E0B9CC80474)

Only the FA model is supported in API version 8 and earlier versions. If you want to use API version 8 or earlier, change the API for constructing the Worker instance and the API for creating an object in the Worker thread for communicating with the host thread.

## FA Model

The following uses API version 9 as an example.

// Main thread (The following assumes that the workers directory and pages directory are at the same level.)
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// Create a Worker instance in the host thread.
const workerInstance = new worker.ThreadWorker("workers/worker.ets");

// The host thread transfers information to the Worker thread.
const buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, \[buffer\]);

// The host thread receives information from the Worker thread.
workerInstance.onmessage = (e: MessageEvents): void => {
    // data carries the information sent by the Worker thread.
    let data: Int8Array = e.data;
    console.info("main thread onmessage");

    // Terminate the Worker instance.
    workerInstance.terminate();
}

// Call onexit().
workerInstance.onexit = (code) => {
    console.info("main thread terminate");
}

workerInstance.onerror = (err: ErrorEvent) => {
    console.error("main error message " + err.message);
}

// worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// Create an object in the Worker thread for communicating with the host thread.
const workerPort = worker.workerPort;

// The Worker thread receives information from the host thread.
workerPort.onmessage = (e: MessageEvents): void => {
    // data carries the information sent by the host thread.
    let data: ArrayBuffer = e.data;
    const view = new Int8Array(data).fill(3);
    console.info("worker.ets onmessage");

    // The Worker thread sends information to the host thread.
    workerPort.postMessage(view);
}

// Trigger a callback when an error occurs in the Worker thread.
workerPort.onerror = (err: ErrorEvent) => {
    console.error("worker.ets onerror");
}

Add the following configuration to the module-level **entry/build-profile.json5** file:

  "buildOption": {
    "sourceOption": {
      "workers": \[
        "./src/main/ets/entryability/workers/worker.ets"
      \]
    }
  }

## Stage Model

The following uses API version 18 as an example.

// Index.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // Create a Worker instance in the host thread.
            const workerInstance = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
            // The host thread transfers information to the Worker thread.
            const buffer = new ArrayBuffer(8);
            workerInstance.postMessage(buffer);
            // The host thread receives information from the Worker thread.
            workerInstance.onmessage = (e: MessageEvents): void => {
              // data carries the information sent by the Worker thread.
              let data: Int8Array = e.data;
              console.info("main thread data is  " + data);
              // Terminate the Worker instance.
              workerInstance.terminate();
            }
            // Call onexit().
            workerInstance.onexit = (code) => {
              console.info("main thread terminate");
            }

            workerInstance.onAllErrors = (err: ErrorEvent) => {
              console.error("main error message " + err.message);
            }
          })
      }
      .width('100%')
      .height('100%')
    }
  }
}

// Worker.ets
import { worker, MessageEvents, ErrorEvent } from '@kit.ArkTS';

// Create an object in the Worker thread for communicating with the host thread.
const workerPort = worker.workerPort;

// The Worker thread receives information from the host thread.
workerPort.onmessage = (e: MessageEvents): void => {
  // data carries the information sent by the host thread.
  let data: ArrayBuffer = e.data;
  // Write data to the received buffer.
  const view = new Int8Array(data).fill(3);
  // The Worker thread sends information to the host thread.
  workerPort.postMessage(view);
}

// Trigger a callback when an error occurs in the Worker thread.
workerPort.onerror = (err: ErrorEvent) => {
  console.error("worker.ets onerror" + err.message);
}

Add the following configuration to the module-level **entry/build-profile.json5** file:

  "buildOption": {
    "sourceOption": {
      "workers": \[
        "./src/main/ets/workers/Worker.ets"
      \]
    }
  }

## Using dispatchEvent with addEventListener

// Index.ets
import { worker, MessageEvents } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page\_text\_font\_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");

          // Usage 1:
          workerInstance.on("alert\_on", () => {
            console.info("alert listener callback: alert\_on");
          })
          workerInstance.once("alert\_once", () => {
            console.info("alert listener callback: alert\_once");
          })
          workerInstance.addEventListener("alert\_add", () => {
            console.info("alert listener callback: alert\_add");
          })

          // The event listener created by once is removed after being executed once.
          workerInstance.dispatchEvent({type:"alert\_once", timeStamp:0}); // timeStamp is not supported yet.
          // The event listener created by on will not be proactively deleted.
          workerInstance.dispatchEvent({type: "alert\_on", timeStamp: 0}); // timeStamp is not supported yet.
          workerInstance.dispatchEvent({type: "alert\_on", timeStamp: 0}); // timeStamp is not supported yet.
          // The event listener created by addEventListener will not be proactively deleted.
          workerInstance.dispatchEvent({type: "alert\_add", timeStamp: 0}); // timeStamp is not supported yet.
          workerInstance.dispatchEvent({type: "alert\_add", timeStamp: 0}); // timeStamp is not supported yet.

          // Usage 2:
          // The event type can be customized, and the special types "message", "messageerror", and "error" exist.
          // When type = "message", the event handler defined by onmessage will also be executed.
          // When type = "messageerror", the event handler defined by onmessageerror will also be executed.
          // When type = "error", the event handler defined by onerror will also be executed.
          // removeEventListener or off can be used to remove an event listener that is created by addEventListener, on, or once.

          workerInstance.addEventListener("message", () => {
            console.info("message listener callback");
          })
          workerInstance.onmessage = (e: MessageEvents): void => {
            console.info("onmessage : message listener callback");
          }
          // When dispatchEvent is called to distribute the "message" event, the callback passed in addEventListener and onmessage will be invoked.
          workerInstance.dispatchEvent({type: "message", timeStamp: 0}); // timeStamp is not supported yet.

          // Send a message to the Worker thread.
          workerInstance.postMessage("test");
        })
    }
    .height('100%')
    .width('100%')
  }
}

// worker.ets
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  console.info("worker thread recv data is: ", event.data);
  let data: string = event.data;
  const workerHandler1 = () => console.info("Handler 1 is: ", data);
  const workerHandler2 = () => console.info("Handler 2 is: ", data);

  // Register two listeners.
  workerPort.addEventListener("workerListener", workerHandler1);
  workerPort.addEventListener("workerListener", workerHandler2);

  // Register two listeners for workerListener. Both listeners are executed.
  workerPort.dispatchEvent({type: "workerListener", timeStamp: 0}); // timeStamp is not supported yet.

  // Remove the workerHandler1 listener.
  workerPort.removeEventListener("workerListener", workerHandler1); // timeStamp is not supported yet.

  // The workerHandler1 listener has been removed, and only workerHandler2 is executed.
  workerPort.dispatchEvent({type: "workerListener", timeStamp: 0}); // timeStamp is not supported yet.

  // Remove all event listeners.
  workerPort.removeAllListener();
};
