# Timer

The **Timer** module provides basic timer capabilities. You can use the APIs of this module to execute functions at the specified time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/7HRq8yXHQbi3q17uZaaxGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062526Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAFABE68D0C8E40B039F2754C3134FC8CD8CC2BE29F4C4EB19B09CFAFAEF6ECA)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

When a timer is used on the UI, the timer triggering mechanism is controlled by the underlying principles of the UI. If the UI is switched to the background, the timer will be suspended.

#### setTimeout

setTimeout(handler: Function | string, delay?: number, ...arguments: any\[\]): number

Sets a timer for the system to call a function after the timer goes off.

The timer is automatically deleted after callback execution, or you may manually delete it via the **clearTimeout()** API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | Function | string | Yes | 
When the type is function, this parameter specifies the callback function to be invoked upon the timer's expiration.

When the type is string, error information is printed with no additional processing.

 |
| delay | number | No | 

Number of milliseconds delayed before the execution. It is recommended that an integer be passed in; a decimal will be rounded down.

If this parameter is omitted, the default value of **0** is used.

**NOTE**

1\. This timer is not a precise timer, and there may be a discrepancy between the actual delay and the expected delay.

2\. If the value is less than 1, it will be defaulted to **0**.

3\. The value is subject to system limitations. If it exceeds 2^31 – 1, the value will be **0**.

 |
| ...arguments | any\[\] | No | 

Additional parameters that are passed to **handler** only when **handler** is of the function type.

If the number of arguments is less than that of the **handler** function parameters, the parameters that are not overwritten by arguments are set to **undefined**.

If the number of arguments exceeds that of the **handler** function parameters, the excess arguments will be ignored. However, they can still be accessed via the built-in arguments object within the **handler** function.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | ID of the timer. The timer ID is shared by processes and is an integer starting from 0 in ascending order. |

**Example 1**: no parameters

setTimeout(() => {
  console.info('delay 1s');
}, 1000);

**Example 2**: **handler** function parameters match arguments count

function myFunction(param1: string, param2: string) {
  console.info(param1, param2);
}
setTimeout(myFunction, 1000, 'Hello', 'World');

**Example 3**: fewer **handler** function parameters than arguments

function myFunction(a: string, b: string) {
  console.info(a);
  // Output: hello
  console.info(b);
  // Output: world
  console.info(JSON.stringify(arguments));
  // Output: {"0":"hello","1":"world","2":"c++","3":"js"}
}
setTimeout(myFunction, 1000, 'hello', 'world', 'C++', 'js');

**Example 4**: more **handler** function parameters than arguments

function myFunction(a: string, b: string) {
  console.info(a);
  // Output: hello
  console.info(b);
  // Output: undefined
  console.info(JSON.stringify(arguments));
  // Output: {"0":"hello"}
}
setTimeout(myFunction, 1000, 'hello');

#### clearTimeout

clearTimeout(timeoutID?: number): void

Cancels a timer set via **setTimeout()**.

The timer object is stored in the thread where the timer is created and must be deleted in that thread.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeoutID | number | No | The ID of the timer to be canceled, which must be the same as the return value of **setTimeout()**. If this parameter is omitted or the specified timer ID does not exist, no timer will be canceled. |

**Example**

let timeoutID = setTimeout(() => {
  console.info('do after 1s delay.');
}, 1000);
clearTimeout(timeoutID);

#### setInterval

setInterval(handler: Function | string, delay: number, ...arguments: any\[\]): number

Sets a repeating timer for the system to repeatedly call a function at a fixed interval.

The timer can only be manually deleted when the **clearInterval** API is called.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | Function | string | Yes | 
When the type is function, this parameter specifies the callback function to be invoked upon the timer's expiration.

When the type is string, error information is printed with no additional processing.

 |
| delay | number | Yes | 

Number of milliseconds delayed before the execution. It is recommended that an integer be passed in; a decimal will be rounded down.

If this parameter is omitted, the default value of **0** is used.

**NOTE**

1\. This timer is not a precise timer, and there may be a discrepancy between the actual delay and the expected delay.

2\. If the value is less than 1, it will be defaulted to **0**.

3\. The value is subject to system limitations. If it exceeds 2^31 – 1, the value will be **0**.

 |
| ...arguments | any\[\] | No | 

Additional parameters that are passed to **handler** only when **handler** is of the function type.

If the number of arguments is less than that of the **handler** function parameters, the parameters that are not overwritten by arguments are set to **undefined**.

If the number of arguments exceeds that of the **handler** function parameters, the excess arguments will be ignored. However, they can still be accessed via the built-in arguments object within the **handler** function.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | ID of the timer. The timer ID is shared by processes and is an integer starting from 0 in ascending order. |

**Example**

setInterval(() => {
  console.info('do every 1s.');
}, 1000);

#### clearInterval

clearInterval(intervalID?: number): void

Cancels the repeated timer set via **setInterval()**.

The timer object is stored in the thread where the timer is created and must be deleted in that thread.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| intervalID | number | No | ID of the repeated timer to be canceled, which must match the return value of the **setInterval** API used to create the repeated timer. If this parameter is omitted or the repeated timer ID does not exist, no timer will be canceled. |

**Example**

let intervalID = setInterval(() => {
  console.info('do every 1s.');
}, 1000);
clearInterval(intervalID);

#### Other Description

## Timeout Delay

If the page is engaged in other operations, the timeout may be later than expected. The function or code snippet passed to **setTimeout** is executed in the next tick. Example:

function foo() {
  console.info('OH test foo is called')
}
setTimeout(foo, 0);
console.info('After OH test setTimeout')

// output
After OH test setTimeout
OH test foo is called

Although a 0 ms delay is specified for **setTimeout()**, the task is not executed immediately. Instead, it is placed in the queue and waits for the next event loop tick. The functions in the queue can be executed only after the ongoing code execution is complete. As such, the final execution sequence may differ from the expected sequence.

## Maximum Delay

The timer internally stores the delay as a 32-bit signed integer. If the delay is greater than 2147483647 ms (about 24.8 days), the overflow occurs and the timer is executed immediately.

## Timer Suspension

The timer triggering mechanism is controlled by the bottom-layer task scheduling. If an application is switched to the background, timers that have reached their set time will not be triggered. Once the application is restored to the foreground, the expired timers will be triggered in sequence. You can run the trace command to check whether the process is still scheduled. If the process is not scheduled, the timer is suspended.

## Timer ID

The **setTimeout()** and **setInterval()** APIs shares an ID pool. This means that, in theory, **clearTimeout()** and **clearInterval()** can be used interchangeably to clear timers. However, to ensure code readability and maintainability, it is advised to use the corresponding clearing method to avoid intermixing.
