# @ohos.util (util)

The util module provides common utility functions, such as [TextEncoder](#textencoder) and [TextDecoder](#textdecoder) for string encoding and decoding, [RationalNumber8+](#rationalnumber8) for rational number operations, [LRUCache9+](#lrucache9) for cache management, [ScopeHelper9+](#scopehelper9) for range determination, [Base64Helper9+](#base64helper9) for Base64 encoding and decoding, [types8+](#types8) for built-in object type check, and [Aspect11+](#aspect11) for instrumentation and replacement on methods.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/GeVjEOnWTd-X2dAgFTurIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADC620E2593F9F510781656B8D22BCEC1BB0D5B9C44F3E57DE0C3AAFAB9B70A1)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { util } from '@kit.ArkTS';

#### util.format9+

format(format: string, ...args: Object\[\]): string

Formats a string by replacing the placeholders in it.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Format string. This string contains zero or more placeholders, which specify the position and format of the arguments to be inserted. |
| ...args | Object\[\] | No | Data used to replace the placeholders in **format**. If **null** is passed in, the first argument is returned by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Format Specifiers**

| Specifier | Description |
| :-- | :-- |
| %s | Converts a parameter into a string for all values except **Object**, **BigInt**, and **\-0**. |
| %d | Converts a parameter into a decimal integer for all values except **Symbol** and **BigInt**. |
| %i | Converts a string into a decimal integer for all values except **Symbol** and **BigInt**. |
| %f | Converts a string into a floating point number for all values except **BigInt** and **Symbol**. |
| %j | Converts a JavaScript object into a JSON string. |
| %o | Converts a JavaScript object into a string, without containing the prototype chain information of the object. |
| %O | Converts a JavaScript object into a string. |
| %c | Valid only in the browser. It is ignored in other environments. |
| %% | Placeholder for escaping the percent sign. |

**Example**

import { util } from '@kit.ArkTS';

interface utilAddressType {
  city: string;
  country: string;
}
interface utilPersonType {
  name: string;
  age: number;
  address: utilAddressType;
}

let name = 'John';
let age = 20;
let formattedString = util.format('My name is %s and I am %s years old', name, age);
console.info(formattedString);
// Output: My name is John and I am 20 years old
let num = 10.5;
formattedString = util.format('The number is %d', num);
console.info(formattedString);
// Output: The number is 10.5.
num = 100.5;
formattedString = util.format('The number is %i', num);
console.info(formattedString);
// Output: The number is 100.
const pi = 3.141592653;
formattedString = util.format('The value of pi is %f', pi);
console.info(formattedString);
// Output: The value of pi is 3.141592653
const obj: Record<string,number | string> = { "name": 'John', "age": 20 };
formattedString = util.format('The object is %j', obj);
console.info(formattedString);
// Output: The object is {"name":"John","age":20}.
const person: utilPersonType = {
  name: 'John',
  age: 20,
  address: {
    city: 'New York',
    country: 'USA'
  }
};
console.info(util.format('Formatted object using %%O: %O', person));
console.info(util.format('Formatted object using %%o: %o', person));
/\*
Output:
Formatted object using %O: { name: 'John',
  age: 20,
  address:
  { city: 'New York',
    country: 'USA' } }
Formatted object using %o: { name: 'John',
  age: 20,
  address:
  { city: 'New York',
    country: 'USA' } }
 \*/
const percentage = 80;
let arg = 'homework';
formattedString = util.format('John finished %d%% of the %s', percentage, arg);
console.info(formattedString);
// Output: John finished 80% of the homework

#### util.errnoToString9+

errnoToString(errno: number): string

Obtains detailed information about a system error code.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| errno | number | Yes | Error code generated. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Detailed information about the error code. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let errnum = -1; // -1 is a system error code.
let result = util.errnoToString(errnum);
console.info("result = " + result);
// Output: result = operation not permitted

**Some error code and message examples**

| Error Code | Message |
| :-- | :-- |
| \-1 | operation not permitted |
| \-2 | no such file or directory |
| \-3 | no such process |
| \-4 | interrupted system call |
| \-5 | i/o error |
| \-11 | resource temporarily unavailable |
| \-12 | not enough memory |
| \-13 | permission denied |
| \-100 | network is down |

#### util.callbackWrapper

callbackWrapper(original: Function): (err: Object, value: Object)=>void

Calls back an asynchronous function. In the callback, the first parameter indicates the cause of the rejection (the value is **null** if the promise has been resolved), and the second parameter indicates the resolved value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/VwgngR_2T66KnFKxDOMDEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD5E7FCD6BC08F7898FF4EAC5CB50BEC7ED200E96A0669626584F5B17BFA1A46)

**original** must be an asynchronous function. If a non-asynchronous function is passed in, the function is not intercepted, but the error message "callbackWrapper: The type of Parameter must be AsyncFunction" is displayed.

This API converts an async function that returns a promise into an error-first callback function. The function returned by this API accepts a callback as its second input parameter. When this method is called, the original function is executed first. When the promise of **original** returns **resolve**, the first parameter of the callback function is **null**, and the second parameter is the value of **resolve**. When the promise of **original** returns **reject**, the first parameter of the callback function is an error object, and the second parameter is **null**. When **original** is a function without input parameters, the first input parameter of the function returned by this API must be an invalid placeholder parameter.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| original | Function | Yes | Asynchronous function. |

**Return value**

| Type | Description |
| :-- | :-- |
| (err: Object, value: Object)=>void | Callback function, in which the first parameter **err** indicates the cause of the rejection (the value is **null** if the promise has been resolved) and the second parameter **value** indicates the resolved value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

async function fn(input: string) {
  return input;
}
let cb = util.callbackWrapper(fn);
cb('hello world', (err : Object, ret : string) => {
  if (err) throw new Error;
  console.info(ret);
});
// Output: hello world

#### util.promisify9+

promisify(original: (err: Object, value: Object) => void): Function

Receives a function that uses the error-first callback mode, that is, uses (err, value) => callback as the last parameter, and uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| original | (err: Object, value: Object) => void | Yes | Function, in which the first parameter **err** indicates the cause of the rejection (the value is **null** if the promise has been resolved) and the second parameter **value** indicates the resolved value. |

**Return value**

| Type | Description |
| :-- | :-- |
| Function | Promise function. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

async function fn() {
  return 'hello world';
}
const addCall = util.promisify(util.callbackWrapper(fn));
(async () => {
  try {
    let res: string = await addCall();
    console.info(res);
    // Output: hello world
  } catch (err) {
    console.info(err);
  }
})();

#### util.generateRandomUUID9+

generateRandomUUID(entropyCache?: boolean): string

Uses a secure random number generator to generate a random universally unique identifier (UUID) of the string type in RFC 4122 version 4. To improve performance, this API uses cached UUIDs by default, in which **entropyCache** is set to **true**. A maximum of 128 random UUIDs can be cached. After all the 128 UUIDs in the cache are used, a new set of UUIDs is generated to maintain their random distribution. If you do not need to use the cached UUID, set **entropyCache** to **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| entropyCache | boolean | No | Whether to use a cached UUID. The value **true** means to use a cached UUID, and **false** means the opposite. The default value is **true**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | A string representing the UUID generated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

let uuid = util.generateRandomUUID(true);
console.info("RFC 4122 Version 4 UUID:" + uuid);
// Output a random UUID.

#### util.generateRandomBinaryUUID9+

generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array

Uses a secure random number generator to generate a random universally unique identifier (UUID) of RFC 4122 version 4.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| entropyCache | boolean | No | Whether to use a cached UUID. The value **true** means to use a cached UUID, and **false** means the opposite. The default value is **true**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | A Uint8Array value representing the UUID generated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

let uuid = util.generateRandomBinaryUUID(true);
console.info(JSON.stringify(uuid));
// Output a random UUID.

#### util.parseUUID9+

parseUUID(uuid: string): Uint8Array

Converts a UUID of the string type generated by **generateRandomUUID** to a UUID generated by **generateRandomBinaryUUID**, as described in RFC 4122.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uuid | string | Yes | A string representing the UUID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | A Uint8Array value representing the UUID parsed. If the parsing fails, **SyntaxError** is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 10200002 | Invalid uuid string. |

**Example**

let uuid = util.parseUUID("84bdf796-66cc-4655-9b89-d6218d100f9c");
console.info("uuid = " + uuid);
// Output: uuid = 132,189,247,150,102,204,70,85,155,137,214,33,141,16,15,156

#### util.printf(deprecated)

printf(format: string, ...args: Object\[\]): string

Formats a string by replacing the placeholders in it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/T9VeP62MTWC_FUKcR1tAOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D209F1C8FCB651EE0B33E5EF24BDB9C3D27AF8194DC8A13E27A8F614E81C761B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [util.format9+](#utilformat9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Format string. |
| ...args | Object\[\] | No | Data used to replace the placeholders in **format**. If **null** is passed in, the first argument is returned by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String containing the formatted values. |

**Example**

let res = util.printf("%s", "hello world!");
console.info(res);
// Output: hello world!

#### util.getErrorString(deprecated)

getErrorString(errno: number): string

Obtains detailed information about a system error code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/tf5IngHoRV2VH9Q9hx8K6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B0468BE188BEF1F5196D7E20AB1CC2165486A932E82BEB73B1DACC61748BD15)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [util.errnoToString9+](#utilerrnotostring9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| errno | number | Yes | Error code generated. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Detailed information about the error code. |

**Example**

let errnum = -1; // -1 is a system error code.
let result = util.getErrorString(errnum);
console.info("result = " + result);
// Output: result = operation not permitted

#### util.promiseWrapper(deprecated)

promiseWrapper(original: (err: Object, value: Object) => void): Object

Receives a function that uses the error-first callback mode, that is, uses (err, value) => callback as the last parameter, and uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/kmTn7Ug-QpCtDDu0zGPKQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90947BF7229285282EEB041C591A8A8C65387C38BB09CF9EE0E3BC2F0D8305F6)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [util.promisify9+](#utilpromisify9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| original | (err: Object, value: Object) => void | Yes | Asynchronous function. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | Promise in the error-first style (that is, (err, value) => ... is called as the last parameter). |

#### util.getHash12+

getHash(object: object): number

Obtains the hash value of an object.

If no hash value has been obtained, a random hash value is generated, saved to the **hash** field of the object, and returned. If a hash value has been obtained, the hash value saved in the **hash** field is returned (the same value is returned for the same object).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| object | object | Yes | Object whose hash value is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Hash value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

interface Person {
  name: string,
  age: number
}
let obj: Person = { name: 'Jack', age: 20 };
let result1 = util.getHash(obj);
console.info('result1 is ' + result1);
let result2 = util.getHash(obj);
console.info('result2 is ' + result2);
// Output: The values of result1 and result2 are the same and are a random hash value.

#### util.getMainThreadStackTrace20+

getMainThreadStackTrace(): string

Obtains the stack trace information of the main thread. A maximum of 64 call frames can be returned.

This API may affect the performance of the main thread. You are advised to use this API only when necessary, such as in log recording, error analysis, or debugging scenarios.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | Stack trace information of the main thread. If the main thread is not executing JavaScript code, an empty string is returned. |

**Example**

let stack = util.getMainThreadStackTrace();
console.info(stack);
// Obtain the stack trace information of the main thread.

#### TextDecoderOptions11+

Describes decoding-related options, which include **fatal** and **ignoreBOM**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fatal | boolean | No | Yes | Whether to display fatal errors. The value **true** means to display fatal errors, and **false** means the opposite. The default value is **false**. |
| ignoreBOM | boolean | No | Yes | Whether to ignore the BOM. The value **true** means to ignore the BOM, and **false** means the opposite. The default value is **false**. |

#### DecodeToStringOptions12+

Describes the behavioral parameters for the **decodeToString** method when decoding byte streams.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stream | boolean | No | Yes | Whether the incomplete byte sequence at the end of the input needs to be appended to the parameter for the next call of **decodeToString**. The value **true** means that the incomplete byte sequence is stored in the internal buffer until the function is called next time. If the value is false, the byte sequence is directly decoded when the function is called currently. The default value is **false**. |

#### DecodeWithStreamOptions11+

Defines whether decoding follows data blocks.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stream | boolean | No | Yes | Whether to allow data blocks in subsequent **decodeWithStream()**. If data is processed in blocks, set this parameter to **true**. If this is the last data block to process or data is not divided into blocks, set this parameter to **false**. The default value is **false**. |

#### Aspect11+

Provides APIs that support Aspect Oriented Programming (AOP). These APIs can be used to perform instrumentation or replacement on class methods.

#### \[h2\]addBefore11+

static addBefore(targetClass: Object, methodName: string, isStatic: boolean, before: Function): void

Inserts a function before a method of a class object. The inserted function is executed in prior to the original method of the class object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetClass | Object | Yes | Target class object. |
| methodName | string | Yes | Name of the method. Read-only methods are not supported. |
| isStatic | boolean | Yes | Whether the method is a static method. The value **true** means a static method, and **false** means an instance method. |
| before | Function | Yes | Function to insert. If the function carries parameters, then the first parameter is the **this** object, which is the target class object (specified by **targetClass**) if **isStatic** is **true** or the instance object of the method if **isStatic** is **false**; other parameters are the parameters carried in the original method. If the function does not carry any parameter, no processing is performed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class MyClass {
  msg: string = 'msg000';
  foo(arg: string): string {
    console.info('foo arg is ' + arg);
    return this.msg;
  }

  static data: string = 'data000';
  static bar(arg: string): string {
    console.info('bar arg is ' + arg);
    return MyClass.data;
  }
}

let asp = new MyClass();
let result = asp.foo('123');
// Output: foo arg is 123
console.info('result is ' + result);
// Output: result is msg000
console.info('asp.msg is ' + asp.msg);
// Output: asp.msg is msg000

util.Aspect.addBefore(MyClass, 'foo', false, (instance: MyClass, arg: string) => {
  console.info('arg is ' + arg);
  instance.msg = 'msg111';
  console.info('msg is changed to ' + instance.msg);
});

result = asp.foo('123');
// Output: arg is 123
// Output: msg is changed to msg111
// Output: foo arg is 123
console.info('result is ' + result);
// Output: result is msg111
console.info('asp.msg is ' + asp.msg);
// Output: asp.msg is msg111

let res = MyClass.bar('456');
// Output: bar arg is 456
console.info('res is ' + res);
// Output: res is data000
console.info('MyClass.data is ' + MyClass.data);
// Output: MyClass.data is data000

util.Aspect.addBefore(MyClass, 'bar', true, (target: Object, arg: string) => {
  console.info('arg is ' + arg);
  let newVal = 'data111';
  Reflect.set(target, 'data', newVal);
  console.info('data is changed to ' + newVal);
});

res = MyClass.bar('456');
// Output: arg is 456
// Output: data is changed to data111
// Output: bar arg is 456
console.info('res is ' + res);
//Output: res is data111
console.info('MyClass.data is ' + MyClass.data);
// Output: MyClass.data is data111

#### \[h2\]addAfter11+

static addAfter(targetClass: Object, methodName: string, isStatic: boolean, after: Function): void

Inserts a function after a method of a class object. The final return value is the return value of the function inserted.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetClass | Object | Yes | Target class object. |
| methodName | string | Yes | Name of the method. Read-only methods are not supported. |
| isStatic | boolean | Yes | Whether the method is a static method. The value **true** means a static method, and **false** means an instance method. |
| after | Function | Yes | Function to insert. If the function carries parameters, then the first parameter is the **this** object, which is the target class object (specified by **targetClass**) if **isStatic** is **true** or the instance object of the method if **isStatic** is **false**; the second parameter is the return value of the original method (**undefined** if the original method does not have a return value); other parameters are the parameters carried by the original method. If the function does not carry any parameter, no processing is performed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class MyClass {
  msg: string = 'msg000';
  foo(arg: string): string {
    console.info('foo arg is ' + arg);
    return this.msg;
  }
}

let asp = new MyClass();
let result = asp.foo('123');
// Output: foo arg is 123
console.info('result is ' + result);
// Output: result is msg000
console.info('asp.msg is ' + asp.msg);
// Output: asp.msg is msg000

util.Aspect.addAfter(MyClass, 'foo', false, (instance: MyClass, ret: string, arg: string): string => {
  console.info('arg is ' + arg);
  console.info('ret is ' + ret);
  instance.msg = 'msg111';
  console.info('msg is changed to ' + instance.msg);
  return 'msg222';
});

result = asp.foo('123');
// Output: foo arg is 123
// Output: arg is 123
// Output: ret is msg000
// Output: msg is changed to msg111
console.info('result is ' + result);
// Output: result is msg222
console.info('asp.msg is ' + asp.msg);
// Output: asp.msg is msg111

// Examples of addBefore() and addAfter()
class AroundTest {
  foo(arg: string) {
    console.info('execute foo with arg ' + arg);
  }
}
util.Aspect.addBefore(AroundTest, 'foo', false, () => {
  console.info('execute before');
});
util.Aspect.addAfter(AroundTest, 'foo', false, () => {
  console.info('execute after');
});

(new AroundTest()).foo('hello');
// Output: execute before
// Output: execute foo with arg hello
// Output: execute after

#### \[h2\]replace11+

static replace(targetClass: Object, methodName: string, isStatic: boolean, instead: Function) : void

Replaces a method of a class object with another function. After the replacement, only the new function logic is executed. The final return value is the return value of the new function.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetClass | Object | Yes | Target class object. |
| methodName | string | Yes | Name of the method. Read-only methods are not supported. |
| isStatic | boolean | Yes | Whether the method is a static method. The value **true** means a static method, and **false** means an instance method. |
| instead | Function | Yes | Function to be used replacement. If the function carries parameters, then the first parameter is the **this** object, which is the target class object (specified by **targetClass**) if **isStatic** is **true** or the instance object of the method if **isStatic** is **false**; other parameters are the parameters carried in the original method. If the function does not carry any parameter, no processing is performed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class MyClass {
  msg: string = 'msg000';
  foo(arg: string): string {
    console.info('foo arg is ' + arg);
    return this.msg;
  }
}

let asp = new MyClass();
let result = asp.foo('123');
// Output: foo arg is 123
console.info('result is ' + result);
// Output: result is msg000
console.info('asp.msg is ' + asp.msg);
// Output: asp.msg is msg000

util.Aspect.replace(MyClass, 'foo', false, (instance: MyClass, arg: string): string => {
  console.info('execute instead');
  console.info('arg is ' + arg);
  instance.msg = 'msg111';
  console.info('msg is changed to ' + instance.msg);
  return 'msg222';
});

result = asp.foo('123');
// Output: execute instead
// Output: arg is 123
// Output: msg is changed to msg111
console.info('result is ' + result);
// Output: result is msg222
console.info('asp.msg is ' + asp.msg);
// Output: asp.msg is msg111

#### TextDecoder

Provides APIs to decode byte arrays into strings. It supports multiple formats, including UTF-8, UTF-16LE, UTF-16BE, ISO-8859, and Windows-1251.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| encoding | string | Yes | No | 
Encoding format.

The following formats are supported: utf-8, ibm866, iso-8859-2, iso-8859-3, iso-8859-4, iso-8859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-8-i, iso-8859-10, iso-8859-13, iso-8859-14, iso-8859-15, koi8-r, koi8-u, macintosh, windows-874, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-1255, windows-1256, windows-1257, windows-1258, x-mac-cyrillic, gbk, gb18030, big5, euc-jp, iso-2022-jp, shift\_jis, euc-kr, utf-16be, utf-16le, gb2312, and iso-8859-1.

 |
| fatal | boolean | Yes | No | Whether to display fatal errors. The value **true** means to display fatal errors, and **false** means the opposite. |
| ignoreBOM | boolean | Yes | No | Whether to ignore the byte order marker (BOM). The default value is **false**, which indicates that the result contains the BOM. |

#### \[h2\]constructor9+

constructor()

A constructor used to create a **TextDecoder** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Example**

let textDecoder = new util.TextDecoder();
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// Output: retStr = utf-8

#### \[h2\]create9+

static create(encoding?: string, options?: TextDecoderOptions): TextDecoder

Creates a **TextDecoder** object. It provides the same function as the deprecated argument constructor.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | No | Encoding format. The default format is **'utf-8'**. |
| options | [TextDecoderOptions](#textdecoderoptions11) | No | Decoding-related options, which include **fatal** and **ignoreBOM**. If this parameter is left empty, the default value is used. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TextDecoder](#textdecoder) | **TextDecoder** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let retStr = textDecoder.encoding;
console.info('retStr = ' + retStr);
// Output: retStr = utf-8

#### \[h2\]decodeToString12+

decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string

Decodes the input content into a string.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/SDgdCuffTiG2ZCRE7jDo3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C25ECD8F0E06048287E4459611127363451106893FAFECD39CABD4D0BE609914)

This API parses the byte whose value is \\0 and converts it into the Unicode character \\u0000 (null character), which does not cause decoding interruption or errors.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | Uint8Array | Yes | Uint8Array object to decode. |
| options | [DecodeToStringOptions](#decodetostringoptions12) | No | Decoding-related options. The default value is **undefined**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

// Sample code for parsing a byte that does not contain \\0
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let decodeToStringOptions: util.DecodeToStringOptions = {
  stream: false
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let uint8 = new Uint8Array(\[0xEF, 0xBB, 0xBF, 0x61, 0x62, 0x63\]);
let retStr = textDecoder.decodeToString(uint8, decodeToStringOptions);
console.info("retStr = " + retStr);
// Output: retStr = abc

// Sample code for parsing a byte containing \\0
let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let decodeToStringOptions: util.DecodeToStringOptions = {
  stream: false
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let uint8 = new Uint8Array(\[97, 98, 0, 99\]);
let retStr = textDecoder.decodeToString(uint8, decodeToStringOptions);
console.info("retStr = " + retStr);
// Output: retStr = abc
let retJson = JSON.stringify(retStr)
console.info("retJson = " + retJson);
// Output: retJson = ab/u0000c

#### \[h2\]decodeWithStream(deprecated)

decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string

Decodes the input content into a string. If **input** is an empty array, **undefined** is returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/s_QQM_-jQgCbo7Alw3X3fQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=500387C33AC2EFAC9D520275832645A5DF17F9FECDF950648BD2B61F7B270B41)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [decodeToString12+](#decodetostring12) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | Uint8Array | Yes | Uint8Array object to decode. |
| options | [DecodeWithStreamOptions](#decodewithstreamoptions11) | No | Decoding-related options. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let textDecoderOptions: util.TextDecoderOptions = {
  fatal: false,
  ignoreBOM : true
}
let decodeWithStreamOptions: util.DecodeWithStreamOptions = {
  stream: false
}
let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
let uint8 = new Uint8Array(6);
uint8\[0\] = 0xEF;
uint8\[1\] = 0xBB;
uint8\[2\] = 0xBF;
uint8\[3\] = 0x61;
uint8\[4\] = 0x62;
uint8\[5\] = 0x63;
console.info("input num:");
let retStr = textDecoder.decodeWithStream(uint8, decodeWithStreamOptions);
console.info("retStr = " + retStr);
// Output: retStr = abc

#### \[h2\]constructor(deprecated)

constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })

A constructor used to create a **TextDecoder** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/qRh0V4WQQjaevAm2Qzvwww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE6760D8E2F612BABE0A32AB0789E64E9C3C8183D1AEFE0679D120C9C8C38833)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [create9+](#create9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | No | Encoding format. The default format is **'utf-8'**. |
| options | { fatal?: boolean; ignoreBOM?: boolean } | No | Decoding-related options, which include **fatal** and **ignoreBOM**. |

**Table 1** options

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fatal | boolean | No | Whether to display fatal errors. The value **true** means to display fatal errors, and **false** means the opposite. The default value is **false**. |
| ignoreBOM | boolean | No | Whether to ignore the BOM. The value **true** means to ignore the BOM, and **false** means the opposite. The default value is **false**. |

**Example**

let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});

#### \[h2\]decode(deprecated)

decode(input: Uint8Array, options?: { stream?: false }): string

Decodes input parameters and outputs the corresponding text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/uQ9nl3mvRWGUv0wZvezAgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28EF095A0B4D091BFA41A09C5F139161E53BD1D6C63EBA9652C700DBA09BA6D4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [decodeToString12+](#decodetostring12) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | Uint8Array | Yes | Uint8Array object to decode. |
| options | { stream?: false } | No | Decoding-related options. |

**Table 2** options

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stream | boolean | No | Whether to allow data blocks in subsequent **decode()**. If data is processed in blocks, set this parameter to **true**. If data is not divided into blocks, set this parameter to **false**. The default value is **false**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String obtained. |

**Example**

let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
let uint8 = new Uint8Array(6);
uint8\[0\] = 0xEF;
uint8\[1\] = 0xBB;
uint8\[2\] = 0xBF;
uint8\[3\] = 0x61;
uint8\[4\] = 0x62;
uint8\[5\] = 0x63;
console.info("input num:");
let retStr = textDecoder.decode(uint8, {stream: false});
console.info("retStr = " + retStr);
// Output: retStr = abc

#### EncodeIntoUint8ArrayInfo11+

Encrypted information, including the number of read characters and the number of written bytes.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| read | number | Yes | No | Number of characters that have been read. |
| written | number | Yes | No | Number of bytes that have been written. |

#### TextEncoder

Provides APIs to encode strings into byte arrays. Multiple encoding formats are supported.

When **TextEncoder** is used for encoding, the number of bytes occupied by a character varies according to the encoding format. You must explicitly specify the encoding format to obtain the required encoding result.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| encoding | string | Yes | No | 
Encoding format.

The following formats are supported: utf-8, gb2312, gb18030, ibm866, iso-8859-1, iso-8859-2, iso-8859-3, iso-8859-4, iso-8859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-8-i, iso-8859-10, iso-8859-13, iso-8859-14, iso-8859-15, koi8-r, koi8-u, macintosh, windows-874, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-1255, windows-1256, windows-1257, windows-1258, gbk, big5, euc-jp, iso-2022-jp, shift\_jis, euc-kr, x-mac-cyrillic, utf-16be, and utf-16le.

The default value is **'utf-8'**.

 |

#### \[h2\]constructor

constructor()

A constructor used to create a **TextEncoder** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Example**

let textEncoder = new util.TextEncoder();

#### \[h2\]constructor9+

constructor(encoding?: string)

A constructor used to create a **TextEncoder** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | No | Encoding format. The default format is **'utf-8'**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

let textEncoder = new util.TextEncoder("utf-8");

#### \[h2\]create12+

static create(encoding?: string): TextEncoder

Creates a **TextEncoder** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | No | Encoding format. The default format is **'utf-8'**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TextEncoder](#textencoder) | **TextEncoder** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

let textEncoder = util.TextEncoder.create("utf-8");

#### \[h2\]encodeInto9+

encodeInto(input?: string): Uint8Array

Encodes the input content into a Uint8Array object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | string | No | String to encode. The default value is an empty string. If the input parameter is an empty string, the return value is undefined. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Uint8Array object obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

let textEncoder = new util.TextEncoder();
let result = textEncoder.encodeInto("\\uD800¥¥");
console.info("result = " + result);
// Output: result = 237,160,128,194,165,194,165

#### \[h2\]encodeIntoUint8Array9+

encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo

Encodes the input content and stores the result into a Uint8Array object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | string | Yes | String to encode. |
| dest | Uint8Array | Yes | Uint8Array object used to store the UTF-8 encoded text. |

**Return value**

| Type | Description |
| :-- | :-- |
| [EncodeIntoUint8ArrayInfo](#encodeintouint8arrayinfo11) | Object obtained. **read** indicates the number of encoded characters, and **written** indicates the number of bytes in the encoded characters. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let textEncoder = new util.TextEncoder();
let buffer = new ArrayBuffer(4);
let uint8 = new Uint8Array(buffer);
let result = textEncoder.encodeIntoUint8Array('abcd', uint8);
console.info("uint8 = " + uint8);
// Output: uint8 = 97,98,99,100
console.info("result.read = " + result.read);
// Output: result.read = 4
console.info("result.written = " + result.written);
// Output: result.written = 4

#### \[h2\]encodeInto(deprecated)

encodeInto(input: string, dest: Uint8Array): { read: number; written: number }

Writes the generated UTF-8 encoded text to an array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/llO1BdjdSnmnlj1EwZHPCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F48D56AF6EEC75FBB495FF6484DEC970D6AA5655AAEFC7786BE51AD0F667203A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [encodeIntoUint8Array9+](#encodeintouint8array9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | string | Yes | String to encode. |
| dest | Uint8Array | Yes | Uint8Array object used to store the UTF-8 encoded text. |

**Return value**

| Type | Description |
| :-- | :-- |
| { read: number; written: number } | Object obtained. **read** indicates the number of encoded characters, and **written** indicates the number of bytes in the encoded characters. |

**Example**

let textEncoder = new util.TextEncoder();
let buffer = new ArrayBuffer(4);
let uint8 = new Uint8Array(buffer);
let result = textEncoder.encodeInto('abcd', uint8);
console.info("uint8 = " + uint8);
// Output: uint8 = 97,98,99,100

#### \[h2\]encode(deprecated)

encode(input?: string): Uint8Array

Encodes the input content in to a Uint8Array object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/s3P9zJ94QYOAunyiQjub4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=486964DB5FF3608D78E000A7C15E2336AF50358A4051BADD0D275EBBEC57005A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [encodeInto9+](#encodeinto9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| input | string | No | String to encode. The default value is an empty string. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Uint8Array object obtained. |

**Example**

let textEncoder = new util.TextEncoder();
let result = textEncoder.encode("\\uD800¥¥");
console.info("result = " + result);
// Output: result = 237,160,128,194,165,194,165

#### RationalNumber8+

Provides APIs to compare rational numbers and obtain numerators and denominators. For example, the **toString()** API can be used to convert a rational number into a string.

#### \[h2\]constructor9+

constructor()

A constructor used to create a **RationalNumber** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Example**

let rationalNumber = new util.RationalNumber();

#### \[h2\]parseRationalNumber9+

static parseRationalNumber(numerator: number,denominator: number): RationalNumber

Creates a **RationalNumber** instance with a given numerator and denominator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/5ZWYFfnlStOeUAIoLu6KsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41B2C3F2D25635ABAACBAE5305D5E405F484C65DC6A0EC01FE08DF0D4B3B7F5C)

The **numerator** and **denominator** parameters must be integers. If a decimal number is passed in, the function is not intercepted, but the error message "parseRationalNumber: The type of Parameter must be integer" is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| numerator | number | Yes | Numerator, which is an integer. Value range: -Number.MAX\_VALUE <= numerator <= Number.MAX\_VALUE. |
| denominator | number | Yes | Denominator, which is an integer. Value range: -Number.MAX\_VALUE <= denominator <= Number.MAX\_VALUE. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RationalNumber](#rationalnumber8) | **RationalNumber** object obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);

#### \[h2\]createRationalFromString8+

static createRationalFromString(rationalString: string): RationalNumber

Creates a **RationalNumber** object based on the given string.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/3Rbr85CDSvWJbl1FxuSDZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EA66A4EF94AEC51D00DEC2EFF54230A326D2835D0D11A2A8BEC0E6009E389F8)

The **rationalString** parameter must be a string. If a decimal string is passed in, the function is not intercepted, but the error message "createRationalFromString: The type of Parameter must be integer string" is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rationalString | string | Yes | String used to create the **RationalNumber** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RationalNumber](#rationalnumber8)​ | **RationalNumber** object obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The type of rationalString must be string. |

**Example**

let rational = util.RationalNumber.createRationalFromString("3/4");

#### \[h2\]compare9+

compare(another: RationalNumber): number​

Compares this **RationalNumber** object with another **RationalNumber** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| another | [RationalNumber](#rationalnumber8) | Yes | Object used to compare with this **RationalNumber** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns **0** if the two objects are equal; returns **1** if the given object is less than this object; return **\-1** if the given object is greater than this object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.compare(rational);
console.info("result = " + result);
// Output: result = -1

#### \[h2\]valueOf8+

valueOf(): number

Obtains the integer or floating-point value of this **RationalNumber** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | An integer or a floating-point number. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.valueOf();
console.info("result = " + result);
// Output: result = 0.5

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.valueOf();
console.info("result = " + result);
// Output: result = 0.5

#### \[h2\]equals8+

equals(obj: Object): boolean

Checks whether this **RationalNumber** object equals the given object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | Object | Yes | Object used to compare with this **RationalNumber** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the two objects are equal; otherwise, **false** is returned. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.equals(rational);
console.info("result = " + result);
// Output: result = false

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.equals(rational);
console.info("result = " + result);
// Output: result = false

#### \[h2\]getCommonFactor9+

static getCommonFactor(number1: number, number2: number): number

Obtains the greatest common divisor of two specified integers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/-9qRtyi1TL6d-LarlzB-Zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36BC7769CAD93150956FD243EEA37AC6079B9673119A65CDB8862BA4DEFE996B)

The **number1** and **number2** parameters must be integers. If a decimal number is passed in, the function is not intercepted, but the error message "getCommonFactor: The type of Parameter must be integer" is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| number1 | number | Yes | Integer type. Value range: -Number.MAX\_VALUE <= number1 <= Number.MAX\_VALUE. |
| number2 | number | Yes | Integer type. Value range: -Number.MAX\_VALUE <= number2 <= Number.MAX\_VALUE. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Greatest common divisor obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let result = util.RationalNumber.getCommonFactor(4,6);
console.info("result = " + result);
// Output: result = 2

#### \[h2\]getNumerator8+

getNumerator(): number

Obtains the numerator of this **RationalNumber** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Numerator of this **RationalNumber** object. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.getNumerator();
console.info("result = " + result);
// Output: result = 1

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.getNumerator();
console.info("result = " + result);
// Output: result = 1

#### \[h2\]getDenominator8+

getDenominator(): number

Obtains the denominator of this **RationalNumber** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Denominator of this **RationalNumber** object. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.getDenominator();
console.info("result = " + result);
// Output: result = 2

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2)
let result = rationalNumber.getDenominator();
console.info("result = " + result);
// Output: result = 2

#### \[h2\]isZero8+

isZero():boolean

Checks whether this **RationalNumber** object is **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value of this **RationalNumber** object is **0**; otherwise, **false** is returned. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isZero();
console.info("result = " + result);
// Output: result = false

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isZero();
console.info("result = " + result);
// Output: result = false

#### \[h2\]isNaN8+

isNaN(): boolean

Checks whether this **RationalNumber** object is a Not a Number (NaN).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if this **RationalNumber** object is a NaN (the denominator and numerator are both **0**); otherwise, **false** is returned. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isNaN();
console.info("result = " + result);
// Output: result = false

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isNaN();
console.info("result = " + result);
// Output: result = false

#### \[h2\]isFinite8+

isFinite():boolean

Checks whether this **RationalNumber** object represents a finite value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if this **RationalNumber** object represents a finite value (the denominator is not **0**); otherwise, **false** is returned. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.isFinite();
console.info("result = " + result);
// Output: result = true

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.isFinite();
console.info("result = " + result);
// Output: result = true

#### \[h2\]toString8+

toString(): string

Obtains the string representation of this **RationalNumber** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | Returns a string in Numerator/Denominator format in normal cases, for example, 3/5; returns **0/1** if the numerator of this object is **0**; returns **Infinity** if the denominator is **0**; returns **NaN** if the numerator and denominator are both **0**. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// Output: result = 1/2

You are advised to use the following code snippet for API version 9 and later versions:

let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
let result = rationalNumber.toString();
console.info("result = " + result);
// Output: result = 1/2

#### \[h2\]constructor(deprecated)

constructor(numerator: number,denominator: number)

A constructor used to create a **RationalNumber** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/z2jc3jdSQbOD4xRKqjMNUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC8A4DE5357D78B75ABAA490A925B8CA02E096AE0EAF7F6A7BA4117AE10C3D7C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [parseRationalNumber9+](#parserationalnumber9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| numerator | number | Yes | Numerator, which is an integer. |
| denominator | number | Yes | Denominator, which is an integer. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);

#### \[h2\]compareTo(deprecated)

compareTo(another: RationalNumber): number​

Compares this **RationalNumber** object with a given object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/6WCdE6rFTdC0y-s_cIgBsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CDE9C7666D766E09342CE69B033D6E0DA180DA40103E23ED687FE1AE659A4D4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [compare9+](#compare9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| another | RationalNumber | Yes | Object used to compare with this **RationalNumber** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns **0** if the two objects are equal; returns **1** if the given object is less than this object; return **\-1** if the given object is greater than this object. |

**Example**

let rationalNumber = new util.RationalNumber(1,2);
let rational = util.RationalNumber.createRationalFromString("3/4");
let result = rationalNumber.compareTo(rational);
console.info("result = " + result);
// Output: result = -1

#### \[h2\]getCommonDivisor(deprecated)

static getCommonDivisor(number1: number,number2: number): number

Obtains the greatest common divisor of two specified integers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/P7ZG7-c8SuKUtnbEeCs0Zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD65B17A77857B9BCD528BFBF1BCE3DC6D55AEBCD4C05DBDCFD0D925CBD9EE07)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getCommonFactor9+](#getcommonfactor9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| number1 | number | Yes | Integer type. |
| number2 | number | Yes | Integer type. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Greatest common divisor obtained. |

#### LRUCache9+

Provides APIs to discard the least recently used data to make rooms for new elements when the cache is full. This class uses the Least Recently Used (LRU) algorithm, which believes that the recently used data may be accessed again in the near future and the least accessed data is the least valuable data and should be removed from the cache.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Total number of values in this cache. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(1, 8);
let result = pro.length;
console.info('result = ' + result);
// Output: result = 2

#### \[h2\]constructor9+

constructor(capacity?: number)

A constructor used to create a **LRUCache** instance. The default capacity of the cache is 64.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| capacity | number | No | Capacity of the cache to create. The default value is **64**, and the maximum value is **2147483647**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

let pro = new util.LRUCache<number, number>();

#### \[h2\]updateCapacity9+

updateCapacity(newCapacity: number): void

Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown. If the total number of values in the cache is greater than the specified capacity, the deletion operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| newCapacity | number | Yes | New capacity of the cache. The maximum value is **2147483647**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.updateCapacity(100);

#### \[h2\]toString9+

toString(): string

Obtains the string representation of this cache.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | String representation of this cache. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
pro.get(3);
console.info(pro.toString());
// Output: LRUCache\[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% \]
// maxSize: maximum size of the cache. hits: number of matched queries. misses: number of mismatched queries. hitRate: matching rate.

#### \[h2\]getCapacity9+

getCapacity(): number

Obtains the capacity of this cache.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Capacity of the cache. |

**Example**

let pro = new util.LRUCache<number, number>();
let result = pro.getCapacity();
console.info('result = ' + result);
// Output: result = 64

#### \[h2\]clear9+

clear(): void

Clears key-value pairs from this cache.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.length;
pro.clear();
let res = pro.length;
console.info('result = ' + result);
console.info('res = ' + res);
// Output: result = 1
// Output: res = 0

#### \[h2\]getCreateCount9+

getCreateCount(): number

Obtains the number of times that an object is created.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of times that objects are created. |

**Example**

// Create the ChildLRUCache class that inherits LRUCache, and override createDefault() to return a non-undefined value.
class ChildLRUCache extends util.LRUCache<number, number> {
  constructor() {
    super();
  }

  createDefault(key: number): number {
    return key;
  }
}
let lru = new ChildLRUCache();
lru.put(2, 10);
lru.get(3);
lru.get(5);
let res = lru.getCreateCount();
console.info('res = ' + res);
// Output: res = 2

#### \[h2\]getMissCount9+

getMissCount(): number

Obtains the number of times that the queried values are mismatched.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of times that the queried values are mismatched. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
let result = pro.getMissCount();
console.info('result = ' + result);
// Output: result = 0

#### \[h2\]getRemovalCount9+

getRemovalCount(): number

Obtains the number of times that key-value pairs in the cache are recycled.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of times that key-value pairs in the cache are recycled. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.updateCapacity(2);
pro.put(50, 22);
let result = pro.getRemovalCount();
console.info('result = ' + result);
// Output: result = 0

#### \[h2\]getMatchCount9+

getMatchCount(): number

Obtains the number of times that the queried values are matched.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of times that the queried values are matched. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.get(2);
let result = pro.getMatchCount();
console.info('result = ' + result);
// Output: result = 1

#### \[h2\]getPutCount9+

getPutCount(): number

Obtains the number of additions to this cache.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of additions to the cache. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.getPutCount();
console.info('result = ' + result);
// Output: result = 1

#### \[h2\]isEmpty9+

isEmpty(): boolean

Checks whether this cache is empty.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the cache does not contain any value. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.isEmpty();
console.info('result = ' + result);
// Output: result = false

#### \[h2\]get9+

get(key: K): V | undefined

Obtains the value of a key. If the key is not in the cache, [createDefault9+](#createdefault9) is called to create the key. If the value specified in **createDefault** is not **undefined**, [afterRemoval9+](#afterremoval9) is called to return the value specified in **createDefault**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key based on which the value is queried. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | undefined | Value of the key. If no match is found, the value specified in **createDefault** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result  = pro.get(2);
console.info('result = ' + result);
// Output: result = 10

#### \[h2\]put9+

put(key: K,value: V): V

Adds a key-value pair to this cache and returns the value associated with the key. If the total number of values in the cache is greater than the specified capacity, the deletion operation is performed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key of the key-value pair to add. |
| value | V | Yes | Value of the key-value pair to add. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | Value of the key-value pair added. If the key or value is empty, an exception is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new util.LRUCache<number, number>();
let result = pro.put(2, 10);
console.info('result = ' + result);
// Output: result = 10

#### \[h2\]values9+

values(): V\[\]

Obtains all values in this cache, listed from the least to the most recently accessed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| V\[\] | The list of all values in this cache, listed from the least to the most recently accessed. |

**Example**

let pro = new util.LRUCache<number, string>();
pro.put(1, 'A');
pro.put(2, "B");
pro.put(3, 'C');
pro.put(4, 'D')
pro.put(5, 'E')
pro.put(6, 'F')
let result = pro.values();
console.info('result = ' + result);
// Output: result = A,B,C,D,E,F
pro.get(1);
pro.get(2);
result = pro.values();
console.info('result = ' + result);
// Output: result = C,D,E,F,A,B

#### \[h2\]keys9+

keys(): K\[\]

Obtains all keys in this cache, listed from the least to the most recently accessed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| K\[\] | The list of all keys in this cache, listed from the least to the most recently accessed. |

**Example**

let pro = new util.LRUCache<number, string>();
pro.put(1, 'A');
pro.put(2, "B");
pro.put(3, 'C');
pro.put(4, 'D')
pro.put(5, 'E')
pro.put(6, 'F')
let result = pro.keys();
console.info('result = ' + result);
// Output: result = 1,2,3,4,5,6
pro.get(5);
pro.get(3);
result = pro.keys();
console.info('result = ' + result);
// Output: result = 1,2,4,6,5,3

#### \[h2\]remove9+

remove(key: K): V | undefined

Removes a key and its associated value from this cache and returns the value associated with the key. If the key does not exist, **undefined** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | undefined | Returns an **Optional** object containing the removed key-value pair if the key exists in the cache; returns **undefined** if the key does not exist; throws an error if **null** is passed in for **key**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.remove(20);
console.info('result = ' + result);
// Output: result = undefined

#### \[h2\]afterRemoval9+

afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void

Performs subsequent operations after a value is removed. The subsequent operations must be implemented by developers. This API is called during deletion operations, such as [get9+](#get9), [put9+](#put9), [remove9+](#remove9), [clear9+](#clear9), and [updateCapacity9+](#updatecapacity9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/mEpxuXs1RBaM9AekHga6pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DDB3FBC6CCB1F278F9F419BEB77F8961845742F7DCEA6FE1472F9C27D4FA902)

If the callback method is executed after [clear9+](#clear9) and [updateCapacity9+](#updatecapacity9) are called and the input **key** and **value** parameters are of the MapIterator type, perform subsequent operations by referring to example 2.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEvict | boolean | Yes | Whether the capacity is insufficient. If the value is **true**, this API is called due to insufficient capacity. |
| key | K | Yes | Key removed. |
| value | V | Yes | Value removed. |
| newValue | V | Yes | New value for the key if the **put()** method is called and the key to be added already exists. In other cases, this parameter is left blank. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example 1**

class ChildLRUCache<K, V> extends util.LRUCache<K, V> {
  constructor(capacity?: number) {
    super(capacity);
  }

  afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void {
    if (isEvict === true) {
      console.info('key = ' + key);
      // Output: key = 1
      console.info('value = ' + value);
      // Output: value = 1
      console.info('newValue = ' + newValue);
      // Output: newValue = null
    }
  }
}
let lru = new ChildLRUCache<number, number>(2);
lru.put(1, 1);
lru.put(2, 2);
lru.put(3, 3);

**Example 2**

class TestClass {
  str:string = '';
  constructor(input: string) {
    this.str = input;
  }
}

class ChildLRUCache extends util.LRUCache<string, TestClass> {
  constructor(capacity?: number) {
    super(capacity);
  }

  afterRemoval(isEvict: boolean, key: string, value: TestClass, newValue: TestClass): void {
    if(value.toString().indexOf('\[object Map Iterator\]') >= 0) {
      console.info('Entered via clear');
      console.info('isEvict = ' + isEvict);
      const keysIterator = (key as ESObject as IterableIterator<string>);
      const valuesIterator = (value as ESObject as IterableIterator<TestClass>);

      let keyEntry = keysIterator.next();
      let valueEntry = valuesIterator.next();
      while (!keyEntry.done && !valueEntry.done) {
        console.info(\`key = ${keyEntry.value}, valueStr = ${valueEntry.value.str}\`);
        keyEntry = keysIterator.next();
        valueEntry = valuesIterator.next();
      }
    } else {
      console.info('Entered via put');
      console.info('isEvict = ' + isEvict);
      console.info('key = ' + key + '  valueStr = ' + value.str);
    }
  }
}
let test1 = new TestClass('testA');
let test2 = new TestClass('testB');
let test3 = new TestClass('testC');
let lru = new ChildLRUCache(2);
lru.put('aa', test1);
lru.put('bb', test2);
lru.put('cc', test3);    // Remove the key-value pair for 'aa'.
lru.clear();             // Clear the entire cache buffer.
/\*
Output: Entered via put.
         isEvict = true
         key = aa  valueStr = testA
         Entered via clear.
         isEvict = false
         key = bb, valueStr = testB
         key = cc, valueStr = testC
 \*/

#### \[h2\]contains9+

contains(key: K): boolean

Checks whether this cache contains the specified key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the cache contains the specified key; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
let result = pro.contains(2);
console.info('result = ' + result);
// Output: result = true

#### \[h2\]createDefault9+

createDefault(key: K): V

Performs subsequent operations if no key is matched in the cache and returns the value (**undefined** by default) associated with the key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | Value of the key. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let pro = new util.LRUCache<number, number>();
let result = pro.createDefault(50);
console.info('result = ' + result);
// Output: result = undefined

#### \[h2\]entries9+

entries(): IterableIterator<\[K, V\]>

Returns an iterator object that traverses all key-value pairs (\[key, value\]) in this object in the insertion order.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[K, V\]> | Iterable array. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(3, 15);
let pair = pro.entries();
for (let value of pair) {
  console.info(value\[0\]+ ', '+ value\[1\]);
}
// Output:
// 2, 10
// 3, 15

#### \[h2\]\[Symbol.iterator\]9+

\[Symbol.iterator\](): IterableIterator<\[K, V\]>

Obtains a two-dimensional array in key-value pairs.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[K, V\]> | Two-dimensional array in key-value pairs. |

**Example**

let pro = new util.LRUCache<number, number>();
pro.put(2, 10);
pro.put(3, 15);

for (let value of pro) {
  console.info(value\[0\]+ ', '+ value\[1\]);
}
// Output:
// 2, 10
// 3, 15

#### ScopeComparable8+

The values of the **ScopeComparable** type are used to implement the **compareTo** method. Therefore, ensure that the input parameters are comparable.

**System capability**: SystemCapability.Utils.Lang

#### \[h2\]compareTo8+

compareTo(other: ScopeComparable): boolean

Compares two values and returns a Boolean value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| other | [ScopeComparable](#scopecomparable8) | Yes | The other value to be compared with the current value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the current value is greater than or equal to the input value; otherwise, **false** is returned. |

**Example**

Create a class to implement the **compareTo** method. The **Temperature** class is used as an example in the following sample code.

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

#### ScopeType8+

type ScopeType = ScopeComparable | number

Defines the type of values in a **Scope** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Type | Description |
| :-- | :-- |
| number | The value type is a number. |
| [ScopeComparable](#scopecomparable8) | The value type is ScopeComparable. |

#### ScopeHelper9+

Provides APIs to define the valid range of a field. The constructor of this class creates comparable objects with lower and upper limits.

#### \[h2\]constructor9+

constructor(lowerObj: ScopeType, upperObj: ScopeType)

A constructor used to create a **ScopeHelper** object with the specified upper and lower limits.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lowerObj | [ScopeType](#scopetype8) | Yes | Lower limit of the **Scope** object. |
| upperObj | [ScopeType](#scopetype8) | Yes | Upper limit of the **Scope** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}
let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = \[30, 40\]

#### \[h2\]toString9+

toString(): string

Obtains a string representation that contains this **Scope**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | String representation containing the **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]intersect9+

intersect(range: ScopeHelper): ScopeHelper

Obtains the intersection of this **Scope** and the given **Scope**. If the intersection is empty, an exception is thrown.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [ScopeHelper](#scopehelper9) | Yes | **Scope** specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeHelper](#scopehelper9) | Intersection of this **Scope** and the given **Scope**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
let result = range.intersect(rangeFir);
console.info("result = " + result);
// Output: result = \[35, 39\]

#### \[h2\]intersect9+

intersect(lowerObj:ScopeType,upperObj:ScopeType):ScopeHelper

Obtains the intersection of this **Scope** and the given lower and upper limits. If the intersection is empty, an exception is thrown.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lowerObj | [ScopeType](#scopetype8) | Yes | Lower limit. |
| upperObj | [ScopeType](#scopetype8) | Yes | Upper limit. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeHelper](#scopehelper9) | Intersection of this **Scope** and the given lower and upper limits. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.intersect(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = \[35, 39\]

#### \[h2\]getUpper9+

getUpper(): ScopeType

Obtains the upper limit of this **Scope**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeType](#scopetype8) | Upper limit of this **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.getUpper();
console.info("result = " + result);
// Output: result = 40

#### \[h2\]getLower9+

getLower(): ScopeType

Obtains the lower limit of this **Scope**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeType](#scopetype8) | Lower limit of this **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.getLower();
console.info("result = " + result);
// Output: result = 30

#### \[h2\]expand9+

expand(lowerObj: ScopeType,upperObj: ScopeType): ScopeHelper

Obtains the union set of this **Scope** and the given lower and upper limits.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lowerObj | [ScopeType](#scopetype8) | Yes | Lower limit. |
| upperObj | [ScopeType](#scopetype8) | Yes | Upper limit. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeHelper](#scopehelper9) | Union set of this **Scope** and the given lower and upper limits. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.expand(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]expand9+

expand(range: ScopeHelper): ScopeHelper

Obtains the union set of this **Scope** and the given **Scope**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [ScopeHelper](#scopehelper9) | Yes | **Scope** specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeHelper](#scopehelper9) | Union set of this **Scope** and the given **Scope**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.ScopeHelper(tempLower, tempUpper);
let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
let result = range.expand(rangeFir);
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]expand9+

expand(value: ScopeType): ScopeHelper

Obtains the union set of this **Scope** and the given value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScopeType](#scopetype8) | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeHelper](#scopehelper9) | Union set of this **Scope** and the given value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.expand(tempMiDF);
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]contains9+

contains(value: ScopeType): boolean

Checks whether a range is within this **Scope**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScopeType](#scopetype8) | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is within this **Scope**; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// Output: result = true

#### \[h2\]contains9+

contains(range: ScopeHelper): boolean

Checks whether a range is within this **Scope**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [ScopeHelper](#scopehelper9) | Yes | **Scope** specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the range is within this **Scope**; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.ScopeHelper(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.ScopeHelper(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// Output: result = false

#### \[h2\]clamp9+

clamp(value: ScopeType): ScopeType

Limits a value to this **Scope**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScopeType](#scopetype8) | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeType](#scopetype8) | Returns **lowerObj** if the specified value is less than the lower limit; returns **upperObj** if the specified value is greater than the upper limit; returns the specified value if it is within this **Scope**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.ScopeHelper(tempLower, tempUpper);
let result = range.clamp(tempMiDF);
console.info("result = " + result);
// Output: result = 35

#### Base64Helper9+

Provides encoding and decoding for Base64 and Base64URL. The Base64 encoding table contains 64 characters, which are the uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and the special characters plus sign (+) and slash (/). During encoding, the original data is divided into groups of three bytes, and each group contains a 6-bit number. Then, the corresponding characters in the Base64 encoding table are used to represent these numbers. If the last group contains only one or two bytes, the equal sign (=) is used for padding. The Base64 URL encoding table contains 64 characters, including the uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), hyphens (-), and underscores (\_). The Base64 URL encoding result does not contain equal signs (=).

#### \[h2\]constructor9+

constructor()

A constructor used to create a **Base64Helper** instance.

**System capability**: SystemCapability.Utils.Lang

**Atomic service API**: This API can be used in atomic services since API version 11.

**Example**

let base64 = new util.Base64Helper();

#### \[h2\]encodeSync9+

encodeSync(src: Uint8Array, options?: Type): Uint8Array

Encodes the input content into a Uint8Array object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |
| options12+ | [Type](#type10) | No | 
Encoding format.

The following values are available:

\- **util.Type.BASIC** (default): Base64 encoding.

\- **util.Type.BASIC\_URL\_SAFE**: Base64URL encoding.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Uint8Array object obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let base64Helper = new util.Base64Helper();
let array = new Uint8Array(\[115,49,51\]);
let result = base64Helper.encodeSync(array);
console.info("result = " + result);
// Output: result = 99,122,69,122

#### \[h2\]encodeToStringSync9+

encodeToStringSync(src: Uint8Array, options?: Type): string

Performs Base64 encoding on the input Uint8Array byte array and returns a string. This method supports multiple encoding formats, including standard Base64 encoding, MIME-compliant Base64 encoding (with line breaks), and URL-safe Base64 encoding.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |
| options10+ | [Type](#type10) | No | 
Encoding format.

The following values are available:

\- **util.Type.BASIC** (default): Base64 encoding. The return value does not contain carriage return characters or newline characters.

\- **util.Type.MIME**: Base64 encoding. If the return value exceeds 76 characters, a line break is inserted every 76 characters, and each line ends with '\\r\\n'. If the return value is fewer than 76 characters, an exception is thrown.

\- **util.Type.BASIC\_URL\_SAFE**: Base64URL encoding. The return value does not contain carriage return characters or newline characters.

\- **util.Type.MIME\_URL\_SAFE**: Base64URL encoding. Each line in the return value contains a maximum of 76 characters and ends with '\\r\\n'.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

// MIME encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array(\[77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101\]);
let result = base64Helper.encodeToStringSync(array, util.Type.MIME);
console.info("result = " + result);
/\*
// Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
 \*/

// BASIC encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array(\[77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101\]);
let result = base64Helper.encodeToStringSync(array, util.Type.BASIC);
console.info("result = " + result);
/\*
Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
 \*/

// MIME\_URL\_SAFE encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array(\[77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101\]);
let result = base64Helper.encodeToStringSync(array, util.Type.BASIC\_URL\_SAFE);
console.info("result = " + result);
/\*
Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
 \*/
// MIME\_URL\_SAFE encoding
let base64Helper = new util.Base64Helper();
let array =
  new Uint8Array(\[77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
    111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
    115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
    114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
    101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
    101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
    101\]);
let result = base64Helper.encodeToStringSync(array, util.Type.MIME\_URL\_SAFE);
console.info("result = " + result);
/\*
// Output: result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
 \*/

#### \[h2\]decodeSync9+

decodeSync(src: Uint8Array | string, options?: Type): Uint8Array

Decodes a string into a Uint8Array object. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | string | Yes | Uint8Array object or string to decode. |
| options10+ | [Type](#type10) | No | 
Decoding format.

The following values are available:

\- **util.Type.BASIC** (default): Base64 decoding.

\- **util.Type.MIME**: Base64 decoding. The input parameter **src** contains carriage return characters and newline characters.

\- **util.Type.BASIC\_URL\_SAFE**: Base64URL decoding.

\- **util.Type.MIME\_URL\_SAFE**: Base64 URL decoding. The input parameter **src** contains carriage return characters and newline characters.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Uint8Array object obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let base64Helper = new util.Base64Helper();
let buff = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\\r\\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\\r\\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\\r\\n';
let result = base64Helper.decodeSync(buff, util.Type.MIME);
console.info("result = " + result);
/\*
Output: result = 77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
 \*/

#### \[h2\]encode9+

encode(src: Uint8Array, options?: Type): Promise<Uint8Array>

Encodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |
| options12+ | [Type](#type10) | No | 
Encoding format.

The following values are available:

\- **util.Type.BASIC** (default): Base64 encoding.

\- **util.Type.BASIC\_URL\_SAFE**: Base64URL encoding.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the Uint8Array object obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let base64Helper = new util.Base64Helper();
let array = new Uint8Array(\[115,49,51\]);
base64Helper.encode(array).then((val) => {
  console.info(val.toString());
  // Output: 99,122,69,122
})

#### \[h2\]encodeToString9+

encodeToString(src: Uint8Array, options?: Type): Promise<string>

Encodes the input content into a string. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |
| options10+ | [Type](#type10) | No | 
Encoding format.

The following values are available:

\- **util.Type.BASIC** (default): Base64 encoding. The return value does not contain carriage return characters or newline characters.

\- **util.Type.MIME**: Base64 encoding. Each line of the return value contains a maximum of 76 characters and ends with '\\r\\n'.

\- **util.Type.BASIC\_URL\_SAFE**: Base64URL encoding. The return value does not contain carriage return characters or newline characters.

\- **util.Type.MIME\_URL\_SAFE**: Base64URL encoding. Each line in the return value contains a maximum of 76 characters and ends with '\\r\\n'.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the string obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let base64Helper = new util.Base64Helper();
let array = new Uint8Array(\[77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101\]);
base64Helper.encodeToString(array, util.Type.MIME).then((val) => {
  console.info(val);
  /\*
  Output: TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
  aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
  aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
   \*/

})

#### \[h2\]decode9+

decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>

Decodes the input content into a Uint8Array object. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | string | Yes | Uint8Array object or string to decode. |
| options10+ | [Type](#type10) | No | 
Decoding format.

The following values are available:

\- **util.Type.BASIC** (default): Base64 decoding.

\- **util.Type.MIME**: Base64 decoding. The input parameter **src** contains carriage return characters and newline characters.

\- **util.Type.BASIC\_URL\_SAFE**: Base64URL decoding.

\- **util.Type.MIME\_URL\_SAFE**: Base64 URL decoding. The input parameter **src** contains carriage return characters and newline characters.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the Uint8Array object obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let base64Helper = new util.Base64Helper();
let array = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\\r\\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\\r\\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\\r\\n';
base64Helper.decode(array, util.Type.MIME).then((val) => {
  console.info(val.toString());
  /\*
  Output: 77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
   \*/
})

#### StringDecoder12+

Provides the capability of decoding binary streams into strings. The following encoding types are supported: utf-8, iso-8859-2, koi8-r, macintosh, windows-1250, windows-1251, gbk, gb18030, big5, utf-16be, and UTF-16le.

#### \[h2\]constructor12+

constructor(encoding?: string)

Constructor used to create a **StringDecoder** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | No | Encoding type of the input data. The default value is **utf-8**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let decoder = new util.StringDecoder();

#### \[h2\]write12+

write(chunk: string | Uint8Array): string

Decodes a string. Any incomplete multi-byte characters at the end of Uint8Array are filtered out from the returned string and stored in an internal buffer for the next call.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| chunk | string | Uint8Array | Yes | String to decode. Decoding is performed based on the input encoding type. If the input is of the Uint8Array type, decoding is performed normally. If the input is of the string type, the parameter is directly returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String decoded. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let decoder = new util.StringDecoder('utf-8');
let input =  new Uint8Array(\[0xE4, 0xBD, 0xA0, 0xE5, 0xA5, 0xBD\]);
const decoded = decoder.write(input);
console.info("decoded:", decoded);
// Output: decoded: Hello, World

#### \[h2\]end12+

end(chunk?: string | Uint8Array): string

Ends the decoding process and returns any remaining input stored in the internal buffer as a string.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| chunk | string | Uint8Array | No | String to decode. The default value is **undefined**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String decoded. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let decoder = new util.StringDecoder('utf-8');
let input = new Uint8Array(\[0xE4, 0xBD, 0xA0, 0xE5, 0xA5, 0xBD\]);
const writeString = decoder.write(input.slice(0, 5));
const endString = decoder.end(input.slice(5));
console.info("writeString:", writeString);
// Output: writeString: Hello
console.info("endString:", endString);
// Output: endString: World

#### Type10+

Enumerates the Base64 encoding formats.

**System capability**: SystemCapability.Utils.Lang

| Name | Value | Description |
| :-- | :-- | :-- |
| BASIC | 0 | Basic format. **Atomic service API**: This API can be used in atomic services since API version 11. |
| MIME | 1 | MIME format. **Atomic service API**: This API can be used in atomic services since API version 11. |
| BASIC\_URL\_SAFE12+ | 2 | 
BASIC\_URL\_SAFE format.

This value is supported since API version 12. **Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MIME\_URL\_SAFE12+ | 3 | 

MIME\_URL\_SAFE format.

This value is supported since API version 12. **Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### types8+

Provides APIs to check different types of built-in objects, such as ArrayBuffer, Map, and Set, so as to avoid exceptions caused by type errors.

#### \[h2\]constructor8+

constructor()

A constructor used to create a **Types** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Example**

let type = new util.types();

#### \[h2\]isAnyArrayBuffer8+

isAnyArrayBuffer(value: Object): boolean

Checks whether the value is of the ArrayBuffer or SharedArrayBuffer type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the ArrayBuffer or SharedArrayBuffer type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isAnyArrayBuffer(new ArrayBuffer(0));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isArrayBufferView8+

isArrayBufferView(value: Object): boolean

Checks whether the value is of the ArrayBufferView type.

**ArrayBufferView** is a type representing any of the following: Int8Array, Int16Array, Int32Array, Uint8Array, Uint8ClampedArray, Uint32Array, Float32Array, **Float64Array**, and DataView.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the ArrayBufferView type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isArrayBufferView(new Int8Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isArgumentsObject8+

isArgumentsObject(value: Object): boolean

Checks whether the value is an **arguments** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is an **arguments** object; otherwise, **false** is returned. |

**Example**

let type = new util.types();
function foo() {
    let result = type.isArgumentsObject(arguments);
    console.info("result = " + result);
}
let f = foo();
// Output: result = true

#### \[h2\]isArrayBuffer8+

isArrayBuffer(value: Object): boolean

Checks whether the value is of the ArrayBuffer type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the ArrayBuffer type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isArrayBuffer(new ArrayBuffer(0));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isAsyncFunction8+

isAsyncFunction(value: Object): boolean

Checks whether the value is an asynchronous function.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is an asynchronous function; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isAsyncFunction(async () => {});
console.info("result = " + result);
// Output: result = true

#### \[h2\]isBooleanObject(deprecated)

isBooleanObject(value: Object): boolean

Checks whether the value is of the Boolean type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/MrkaieJ3TE24CWZPP3FivA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0D44791EE1B382B726A4E588CF89867482578E195054BEDF6ED31EBCB4A47AA)

This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Boolean type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isBooleanObject(new Boolean(true));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isBoxedPrimitive(deprecated)

isBoxedPrimitive(value: Object): boolean

Checks whether the value is of the Boolean, Number, String, or Symbol type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/jt-FwMoLRxScNFOSXR6O_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D81907C3AD140FAC9ABD8620437CC9A56E9B063445B5992F817D46BAB314C37)

This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Boolean, Number, String, or Symbol type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isBoxedPrimitive(new Boolean(false));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isDataView8+

isDataView(value: Object): boolean

Checks whether the value is of the DataView type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the DataView type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
const ab = new ArrayBuffer(20);
let result = type.isDataView(new DataView(ab));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isDate8+

isDate(value: Object): boolean

Checks whether the value is of the Date type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Date type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isDate(new Date());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isExternal8+

isExternal(value: Object): boolean

Checks whether the value is of the native external type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the native external type; otherwise, **false** is returned. |

**Example**

// /entry/src/main/cpp/napi\_init.cpp
#include "napi/native\_api.h"
#include <js\_native\_api.h>
#include <stdlib.h>

napi\_value result;
static napi\_value Testexternal(napi\_env env, napi\_callback\_info info) {
    int\* raw = (int\*) malloc(1024);
    napi\_status status = napi\_create\_external(env, (void\*) raw, NULL, NULL, &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, NULL, "create external failed");
        return NULL;
    }
    return result;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"testexternal", nullptr, Testexternal, nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
// The code for module registration is omitted here. You may need to register the Testexternal method.
...

import testNapi from 'libentry.so';

let type = new util.types();
const data = testNapi.testexternal();
let result = type.isExternal(data);

let result01 = type.isExternal(true);
console.info("result = " + result);
console.info("result01 = " + result01);
// Output: result = true
// Output: result01 = false

#### \[h2\]isFloat32Array8+

isFloat32Array(value: Object): boolean

Checks whether the value is of the Float32Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Float32Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isFloat32Array(new Float32Array());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isFloat64Array8+

isFloat64Array(value: Object): boolean

Checks whether the value is of the Float64Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Float64Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isFloat64Array(new Float64Array());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isGeneratorFunction8+

isGeneratorFunction(value: Object): boolean

Checks whether the value is a generator function.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is a generator function; otherwise, **false** is returned. |

**Example**

// /entry/src/main/ets/pages/test.ts
export function\* foo() {}

import { foo } from './test'

let type = new util.types();
let result = type.isGeneratorFunction(foo);
console.info("result = " + result);
// Output: result = true

#### \[h2\]isGeneratorObject8+

isGeneratorObject(value: Object): boolean

Checks whether the value is a generator object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is a generator object; otherwise, **false** is returned. |

**Example**

// /entry/src/main/ets/pages/test.ts
function\* foo() {}
export const generator = foo();

import { generator } from './test'

let type = new util.types();
let result = type.isGeneratorObject(generator);
console.info("result = " + result);
// Output: result = true

#### \[h2\]isInt8Array8+

isInt8Array(value: Object): boolean

Checks whether the value is of the Int8Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Int8Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isInt8Array(new Int8Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isInt16Array8+

isInt16Array(value: Object): boolean

Checks whether the value is of the Int16Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Int16Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isInt16Array(new Int16Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isInt32Array8+

isInt32Array(value: Object): boolean

Checks whether the value is of the Int32Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Int32Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isInt32Array(new Int32Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isMap8+

isMap(value: Object): boolean

Checks whether the value is of the Map type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Map type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isMap(new Map());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isMapIterator8+

isMapIterator(value: Object): boolean

Checks whether the value is of the MapIterator type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the MapIterator type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
const map : Map<number,number> = new Map();
let result = type.isMapIterator(map.keys());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isNativeError8+

isNativeError(value: Object): boolean

Checks whether the value is of the Error type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Error type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isNativeError(new TypeError());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isNumberObject(deprecated)

isNumberObject(value: Object): boolean

Checks whether the value is of the Number type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/KjMwVbMnTsyx8SypuUCVjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE88B4EAEE84617944CF6EE46BA24EED78993AB2738655B81DE31BA84BA2CD02)

This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Number type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isNumberObject(new Number(0));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isPromise8+

isPromise(value: Object): boolean

Checks whether the value is a promise.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is a promise; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isPromise(Promise.resolve(1));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isProxy8+

isProxy(value: Object): boolean

Checks whether the value is a proxy.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is a proxy; otherwise, **false** is returned. |

**Example**

class Target{
}
let type = new util.types();
const target : Target = {};
const proxy = new Proxy(target, target);
let result = type.isProxy(proxy);
console.info("result = " + result);
// Output: result = true

#### \[h2\]isRegExp8+

isRegExp(value: Object): boolean

Checks whether the value is of the RegExp type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the RegExp type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isRegExp(new RegExp('abc'));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isSet8+

isSet(value: Object): boolean

Checks whether the value is of the Set type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Set type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let set : Set<number> = new Set();
let result = type.isSet(set);
console.info("result = " + result);
// Output: result = true

#### \[h2\]isSetIterator8+

isSetIterator(value: Object): boolean

Checks whether the value is of the SetIterator type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the SetIterator type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
const set : Set<number> = new Set();
let result = type.isSetIterator(set.keys());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isStringObject(deprecated)

isStringObject(value: Object): boolean

Checks whether the value is a string object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/GG7pB6yyQEOggvpjQdFw0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B096FBE18852B5571D1ECF290DEC6FFC66361F959CB429FC6B07FB205CA936AF)

This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is a string object; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isStringObject(new String('foo'));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isSymbolObject(deprecated)

isSymbolObject(value: Object): boolean

Checks whether the value is a symbol object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/LapbmSkKReGjfkOR0wNKHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24CB120C7B18EF45A40C0E7EE59F4C4C5BE777269FDBD20981815444A383B83E)

This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is a symbol object; otherwise, **false** is returned. |

**Example**

// /entry/src/main/ets/pages/test.ts
export const symbols = Symbol('foo');

import { symbols } from './test'

let type = new util.types();
let result = type.isSymbolObject(Object(symbols));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isTypedArray8+

isTypedArray(value: Object): boolean

Checks whether the value is of the TypedArray type.

**TypedArray** is a type representing any of the following: Int8Array, Int16Array, Int32Array, Uint8Array, Uint8ClampedArray, Uint16Array, Uint32Array, Float32Array, Float64Array, BigInt64Array, and BigUint64Array.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the TypedArray type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isTypedArray(new Float64Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isUint8Array8+

isUint8Array(value: Object): boolean

Checks whether the value is of the Uint8Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Uint8Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isUint8Array(new Uint8Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isUint8ClampedArray8+

isUint8ClampedArray(value: Object): boolean

Checks whether the value is of the Uint8ClampedArray type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Uint8ClampedArray type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isUint8ClampedArray(new Uint8ClampedArray(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isUint16Array8+

isUint16Array(value: Object): boolean

Checks whether the value is of the Uint16Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Uint16Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isUint16Array(new Uint16Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isUint32Array8+

isUint32Array(value: Object): boolean

Checks whether the value is of the Uint32Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the Uint32Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isUint32Array(new Uint32Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isWeakMap8+

isWeakMap(value: Object): boolean

Checks whether the value is of the WeakMap type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the WeakMap type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let value : WeakMap<object, number> = new WeakMap();
let result = type.isWeakMap(value);
console.info("result = " + result);
// Output: result = true

#### \[h2\]isWeakSet8+

isWeakSet(value: Object): boolean

Checks whether the value is of the WeakSet type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the WeakSet type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isWeakSet(new WeakSet());
console.info("result = " + result);
// Output: result = true

#### \[h2\]isBigInt64Array8+

isBigInt64Array(value: Object): boolean

Checks whether the value is of the BigInt64Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the BigInt64Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isBigInt64Array(new BigInt64Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isBigUint64Array8+

isBigUint64Array(value: Object): boolean

Checks whether the value is of the BigUint64Array type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the BigUint64Array type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isBigUint64Array(new BigUint64Array(\[\]));
console.info("result = " + result);
// Output: result = true

#### \[h2\]isModuleNamespaceObject8+

isModuleNamespaceObject(value: Object): boolean

Checks whether the value is a module namespace object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is a module namespace object; otherwise, **false** is returned. |

**Example**

// /entry/src/main/ets/pages/test.ts
export function func() {
  console.info("hello world");
}

import \* as nameSpace from './test';

let type = new util.types();
let result = type.isModuleNamespaceObject(nameSpace);
console.info("result = " + result);
// Output: result = true

#### \[h2\]isSharedArrayBuffer8+

isSharedArrayBuffer(value: Object): boolean

Checks whether the value is of the SharedArrayBuffer type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is of the SharedArrayBuffer type; otherwise, **false** is returned. |

**Example**

let type = new util.types();
let result = type.isSharedArrayBuffer(new SharedArrayBuffer(0));
console.info("result = " + result);
// Output: result = true

#### AutoFinalizer<T>22+

AutoFinalizer is a class that provides callback APIs when an ArkTS object is released. By implementing it, you can customize the resource cleanup logic that triggers automatically when an object is reclaimed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/815Eu_kESE2kgKUCDsluNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C5F9FB586CC1F4499FEBCCFC809FD5050DD6A405EB6F6402ACD88FB0AF0AEF7)

AutoFinalizer<T> must be used together with AutoFinalizerCleaner<T>. Implementing AutoFinalizer<T> alone will yield no functionality.

#### \[h2\]onFinalization22+

onFinalization(heldValue: T): void

Defines the resource cleanup callback that triggers automatically when an object is reclaimed.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| heldValue | T | Yes | When the listened object is reclaimed, this value is passed to the onFinalization callback method. |

#### AutoFinalizerCleaner<T>22+

AutoFinalizerCleaner is a utility class that associates an object's lifecycle with resource cleanup logic. Its primary role is to bind an object implementing AutoFinalizer<T> to a specific value, and automatically trigger the resource cleanup callback when the object is reclaimed.

#### \[h2\]register<T>22+

static register<T>(obj: AutoFinalizer<T>, heldValue: T): void

Associates an object implementing AutoFinalizer with an input value, and triggers the resource cleanup callback when the object is reclaimed.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | [AutoFinalizer<T>](#autofinalizert22) | Yes | Object that implements AutoFinalizer. The onFinalization method is called when the object is reclaimed. |
| heldValue | T | Yes | When the listened object is reclaimed, this value is passed to the obj.onFinalization method. |

**Example**

class DeviceManageViewModel implements util.AutoFinalizer<string> {
  constructor(heldValue: string) {
    util.AutoFinalizerCleaner.register(this, heldValue);
  }

  onFinalization(heldValue: string) {
    console.info("onFinalization: ", heldValue);
    // Wait for the garbage collection to be triggered. Once it is triggered, the following result is displayed: onFinalization: test
  }
}

const device = new DeviceManageViewModel("test");

#### LruBuffer(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/d5nRDUH1SFOZMoLVx5qp1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2227E89C46BAA0E9C07DAA5E310FF5765B734981424762881467FB8D6B5EE8A6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache9+](#lrucache9) instead.

#### \[h2\]Properties

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Total number of values in this cache. |

**Example**

let pro : util.LruBuffer<number,number>= new util.LruBuffer();
pro.put(2,10);
pro.put(1,8);
let result = pro.length;
console.info("result = " + result);
// Output: result = 2

#### \[h2\]constructor(deprecated)

constructor(capacity?: number)

A constructor used to create a **LruBuffer** instance. The default capacity of the cache is 64.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Wl7HAb_kQdGqYU40ziSS4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F79EA0B11DF8C241DCADDCCF28AC9C6D8BEB3CFE9385A745FFE675A38D98D2C5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.constructor9+](#constructor9-3) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| capacity | number | No | Capacity of the cache to create. The default value is **64**. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();

#### \[h2\]updateCapacity(deprecated)

updateCapacity(newCapacity: number): void

Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/nWOgCjYaTOGaOTvPtctBaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B50191E4061B82EDA0764DECC26C8918119A42CB5FFA9974CCC88815ECC14C1)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.updateCapacity9+](#updatecapacity9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| newCapacity | number | Yes | New capacity of the cache. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.updateCapacity(100);

#### \[h2\]toString(deprecated)

toString(): string

Obtains the string representation of this cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/FOUAzxgySGqC9765c0gsrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F99A1D3D56315C669F09E05F58AF4ACDF27306B7EA95B0283E9828BA69AFEC61)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.toString9+](#tostring9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | String representation of this cache. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
pro.remove(20);
let result = pro.toString();
console.info("result = " + result);
// Output: result = Lrubuffer\[ maxSize = 64, hits = 1, misses = 0, hitRate = 100% \]

#### \[h2\]getCapacity(deprecated)

getCapacity(): number

Obtains the capacity of this cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/kHSaQCruQeOwgnrOV9Un7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7132001AD1D10FE8CA5D7B1B061C20A35E8F9C42F208E515FDBE79B32C15340C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.getCapacity9+](#getcapacity9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Capacity of the cache. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.getCapacity();
console.info("result = " + result);
// Output: result = 64

#### \[h2\]clear(deprecated)

clear(): void

Clears key-value pairs from this cache. The **afterRemoval()** API will be called to perform subsequent operations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/JQUtytIiSVevH28ElBB2KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=212C9E380AA551999F554A3B44645C8DDDCFFF3FB95865B54D643501E909FA35)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.clear9+](#clear9) instead.

**System capability**: SystemCapability.Utils.Lang

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.length;
pro.clear();

#### \[h2\]getCreateCount(deprecated)

getCreateCount(): number

Obtains the number of return values for **createDefault()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/rE4bNyaGSW-4ocD9htW5ww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2260A12D19B14C08E73697408FF2B28559E873052C1C4C854806C6A44979530)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.getCreateCount9+](#getcreatecount9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of return values for **createDefault()**. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(1,8);
let result = pro.getCreateCount();
console.info("result = " + result);
// Output: result = 0

#### \[h2\]getMissCount(deprecated)

getMissCount(): number

Obtains the number of times that the queried values are mismatched.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/J1L_7D_wTAu2vrLCRuZwag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DECC85E435CC8908CE9A350455E235B3D2355AEBD5EE3261BDB174DB35D50D67)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.getMissCount9+](#getmisscount9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of times that the queried values are mismatched. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
let result = pro.getMissCount();
console.info("result = " + result);
// Output: result = 0

#### \[h2\]getRemovalCount(deprecated)

getRemovalCount(): number

Obtains the number of removals from this cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ST7brSHqSUy1v_5M0Gr6vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04C1F492EEBA656246E744EFB7B6BE16AEA99B7D699E046A56EE92ABE5B8544F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.getRemovalCount9+](#getremovalcount9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of removals from the cache. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.updateCapacity(2);
pro.put(50,22);
let result = pro.getRemovalCount();
console.info("result = " + result);
// Output: result = 0

#### \[h2\]getMatchCount(deprecated)

getMatchCount(): number

Obtains the number of times that the queried values are matched.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/divfn49AQjuFdbzIPMWAfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4062A1B35241D4666D8FB160534A0C2B890A8DBB03D2E42733CE0B61E7AED489)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.getMatchCount9+](#getmatchcount9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of times that the queried values are matched. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
pro.get(2);
let result = pro.getMatchCount();
console.info("result = " + result);
// Output: result = 1

#### \[h2\]getPutCount(deprecated)

getPutCount(): number

Obtains the number of additions to this cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/shOU5kzMQ5Gfi4NC7HQxHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=574DB762BB1463EAAF96DE49C95723C344A278FC18319D9AE3223927750EA0DC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.getPutCount9+](#getputcount9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of additions to the cache. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.getPutCount();
console.info("result = " + result);
// Output: result = 1

#### \[h2\]isEmpty(deprecated)

isEmpty(): boolean

Checks whether this cache is empty.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/6JBYkqC8R--AeYiEq-tRTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4F0A28D230B42A9FA2AC7BD33EE4711C6908D7A5A2EDEFC2E6EAD1999F45BED)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.isEmpty9+](#isempty9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the cache does not contain any value. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.isEmpty();
console.info("result = " + result);
// Output: result = false

#### \[h2\]get(deprecated)

get(key: K): V | undefined

Obtains the value of the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/VDeMKqmCTAmWHwSWb_53OQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43EB5DE767B8AE00ABE39B581C5DA327CC3CF1D12CD1FE78D1C1435220749675)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.get9+](#get9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key based on which the value is queried. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | undefined | Value of the key. If no match is found, **undefined** is returned. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result  = pro.get(2);
console.info("result = " + result);
// Output: result = 10

#### \[h2\]put(deprecated)

put(key: K,value: V): V

Adds a key-value pair to this cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/svnB84CXS1aYRsVzl3AUOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=604DC5C97B5457381DB7195F0A8E8EB62DFA9D28A29DA181DC7397C20B028E65)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.put9+](#put9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key of the key-value pair to add. |
| value | V | Yes | Value of the key-value pair to add. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | Value added. If the key already exists, the existing value is returned; if **null** is passed in for **key** or **value**, an error is thrown. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.put(2,10);
console.info("result = " + result);
// Output: result = 10

#### \[h2\]values(deprecated)

values(): V\[\]

Obtains all values in this cache, listed from the most to the least recently accessed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/29c3hl7LTVOhgIgymm9pbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5549FDF0E47BC6BA5065AC65662171A62650E56B413CE6AF943A4DF7E2099B52)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.values9+](#values9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| V \[\] | All values in the cache, listed from the most to the least recently accessed. |

**Example**

let pro : util.LruBuffer<number|string,number|string> = new util.LruBuffer();
pro.put(2,10);
pro.put(2,"anhu");
pro.put("afaf","grfb");
let result = pro.values();
console.info("result = " + result);
// Output: result = anhu,grfb

#### \[h2\]keys(deprecated)

keys(): K\[\]

Obtains all keys in this cache, listed from the most to the least recently accessed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Bx6s6KOEQTChLTOvSSzU2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49929ECC4987845220B29F34BE22C3B3E5492B705A93D665DB632CE6D73E1B45)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.keys9+](#keys9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| K \[\] | All keys in the cache, listed from the most to the least recently accessed. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.keys();
console.info("result = " + result);
// Output: result = 2

#### \[h2\]remove(deprecated)

remove(key: K): V | undefined

Removes the specified key and its value from this cache.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/7_uFblunRJqAfuzutH8g5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B620B49150706E6F465A0B135B34E8C08C8AB5333F32ED88989DCB3BE4296CD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.remove9+](#remove9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key to remove. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | undefined | **Optional** object containing the removed key-value pair. If the key does not exist, an empty **Optional** object is returned; if **null** is passed in for **key**, an error is thrown. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.remove(20);
console.info("result = " + result);
// Output: result = undefined

#### \[h2\]afterRemoval(deprecated)

afterRemoval(isEvict: boolean,key: K,value: V,newValue: V): void

Performs subsequent operations after a value is removed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/D3ggSbYmTqmNS8o4zzyV-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8FF54DC038BFC830C538DC37AA7D8136BB28A22D6F0FD67BAB838BCB7E42F9B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.afterRemoval9+](#afterremoval9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEvict | boolean | Yes | Whether the capacity is insufficient. If the value is **true**, this API is called due to insufficient capacity. |
| key | K | Yes | Key removed. |
| value | V | Yes | Value removed. |
| newValue | V | Yes | New value for the key if the **put()** method is called and the key to be added already exists. In other cases, this parameter is left blank. |

**Example**

class ChildLruBuffer<K, V> extends util.LruBuffer<K, V> {
  constructor(capacity?: number) {
    super(capacity);
  }

  afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void {
    if (isEvict === true) {
      console.info('key: ' + key);
      // Output: key: 11
      console.info('value: ' + value);
      // Output: value: 1
      console.info('newValue: ' + newValue);
      // Output: newValue: null
    }
  }
}
let lru: ChildLruBuffer<number, number> = new ChildLruBuffer(2);
lru.put(11, 1);
lru.put(22, 2);
lru.put(33, 3);

#### \[h2\]contains(deprecated)

contains(key: K): boolean

Checks whether this cache contains the specified key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/j_QqVeTOR4ij_HuIpGjgJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4910A24399CEDE5CCB292AE7323A35F34CAB30657023CAF640856788B57372C7)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.contains9+](#contains9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the cache contains the specified key; otherwise, **false** is returned. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.contains(20);
console.info('result = ' + result);
// Output: result = false

#### \[h2\]createDefault(deprecated)

createDefault(key: K): V

Creates a value if the value of the specified key is not available.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/rmxQPY1KRUGncOCm4CwAww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF45553B523AF8420B88D3721EB1360D6EEE3D379B9742AE24B6100418585510)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.createDefault9+](#createdefault9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key of which the value is missing. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | Value of the key. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
let result = pro.createDefault(50);

#### \[h2\]entries(deprecated)

entries(): IterableIterator<\[K, V\]>

Obtains a new iterator object that contains all key-value pairs in this object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/HsKipN8fR9-TpYw66GrtCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2A03C0810CB0F70DCC80D1C126FB0BDAEB1B47E63078937BCDEE82AAE29CB42)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.entries9+](#entries9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[K, V\]> | Iterable array. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro.entries();

#### \[h2\]\[Symbol.iterator\](deprecated)

\[Symbol.iterator\](): IterableIterator<\[K, V\]>

Obtains a two-dimensional array in key-value pairs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/ryFlshE0SReG2oWS3x6mKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4471332B89E3443EA7BDEFD5E2A6DA9089CF4346002ABFAFBDDC907894B1BDA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [LRUCache.\[Symbol.iterator\]9+](#symboliterator9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[K, V\]> | Two-dimensional array in key-value pairs. |

**Example**

let pro : util.LruBuffer<number,number> = new util.LruBuffer();
pro.put(2,10);
let result = pro\[Symbol.iterator\]();

#### Scope(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/GbfPcgMoRGKRgv7YDrD6Ow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08B1B92051569A581CDF71BAC37952E4DFFCABF9CEF62FA06156B2FA5A4379D5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper9+](#scopehelper9) instead.

#### \[h2\]constructor(deprecated)

constructor(lowerObj: ScopeType, upperObj: ScopeType)

A constructor used to create a **Scope** object with the specified upper and lower limits.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/yH5g0djsR_WJaRb1kG2p1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27810F9EE0B36E2CF106519D09267E7C3E27F2F8E1F560898D19E986D9A31042)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.constructor9+](#constructor9-4) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lowerObj | [ScopeType](#scopetype8) | Yes | Lower limit of the **Scope** object. |
| upperObj | [ScopeType](#scopetype8) | Yes | Upper limit of the **Scope** object. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
console.info("range = " + range);
// Output: range = \[30, 40\]

#### \[h2\]toString(deprecated)

toString(): string

Obtains a string representation that contains this **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/1AfnDguGTxyMO7dmj68vhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51E2D841A271625A8D1CB8FF00347854763FD24E9408F444873C2D2F4069951A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.toString9+](#tostring9-1) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | String representation containing the **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let result = range.toString();
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]intersect(deprecated)

intersect(range: Scope): Scope

Obtains the intersection of this **Scope** and the given **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/b3S7i1YYS2-RO_HvH9xdrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E983EB306F5C6895B7BA04B502A332BD082A1F9CF2273C45EE537B06607CE2DA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.intersect9+](#intersect9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Scope](#scopedeprecated) | Yes | **Scope** specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Scope](#scopedeprecated) | Intersection of this **Scope** and the given **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let rangeFir = new util.Scope(tempMiDF, tempMidS);
let result = range.intersect(rangeFir );
console.info("result = " + result);
  // Output: result = \[35, 39\]

#### \[h2\]intersect(deprecated)

intersect(lowerObj:ScopeType,upperObj:ScopeType):Scope

Obtains the intersection of this **Scope** and the given lower and upper limits.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/EKO-lgHEQ-idCKyW6fenhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30E9EA1E48BD755FDD51C025B3DF54C0BE8F54B6E236C1B0AFAEFB16C4D6F74F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.intersect9+](#intersect9-1) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lowerObj | [ScopeType](#scopetype8) | Yes | Lower limit. |
| upperObj | [ScopeType](#scopetype8) | Yes | Upper limit. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Scope](#scopedeprecated) | Intersection of this **Scope** and the given lower and upper limits. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.Scope(tempLower, tempUpper);
let result = range.intersect(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = \[35, 39\]

#### \[h2\]getUpper(deprecated)

getUpper(): ScopeType

Obtains the upper limit of this **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/kedwMc5MQ0aXfiIzgEjrBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=533FBC5684EDBCB21D121ADBA5CE947DE722717F2A6B36D88BE13D284B8D98D6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.getUpper9+](#getupper9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeType](#scopetype8) | Upper limit of this **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let result = range.getUpper();
console.info("result = " + result);
// Output: result = 40

#### \[h2\]getLower(deprecated)

getLower(): ScopeType

Obtains the lower limit of this **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Wf2YNhhrQ-C4Wa0phCfagg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BDC5D8164CB159C010E28D1D6B8BAA7E6966526D72E3A17C008553677C9DDFB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.getLower9+](#getlower9) instead.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeType](#scopetype8) | Lower limit of this **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let result = range.getLower();
console.info("result = " + result);
// Output: result = 30

#### \[h2\]expand(deprecated)

expand(lowerObj: ScopeType,upperObj: ScopeType): Scope

Obtains the union set of this **Scope** and the given lower and upper limits.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/ZJpli4t2R9ifc5meapYrNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23C4D9FC4491CB0EAADC7874EBA760F92BAFF525A1205FB9ED637DA5028C0197)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.expand9+](#expand9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| lowerObj | [ScopeType](#scopetype8) | Yes | Lower limit. |
| upperObj | [ScopeType](#scopetype8) | Yes | Upper limit. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Scope](#scopedeprecated) | Union set of this **Scope** and the given lower and upper limits. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.Scope(tempLower, tempUpper);
let result = range.expand(tempMiDF, tempMidS);
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]expand(deprecated)

expand(range: Scope): Scope

Obtains the union set of this **Scope** and the given **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/MCCB45eWRqWH-Qzdjt1Big/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B599C47A3862491F58CEAC9057B4872A34A08927DFFFB8BC1D1B486A20934AFC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.expand9+](#expand9-1) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Scope](#scopedeprecated) | Yes | **Scope** specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Scope](#scopedeprecated) | Union set of this **Scope** and the given **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let tempMidS = new Temperature(39);
let range = new util.Scope(tempLower, tempUpper);
let rangeFir = new util.Scope(tempMiDF, tempMidS);
let result = range.expand(rangeFir);
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]expand(deprecated)

expand(value: ScopeType): Scope

Obtains the union set of this **Scope** and the given value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/RR3glGtXQ3GIG_j5eODSAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECC3BE2C928C5AF6F836ADBD7F3C8D57F528B979F62435E75402453FFD525A8E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.expand9+](#expand9-2) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScopeType](#scopetype8) | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Scope](#scopedeprecated) | Union set of this **Scope** and the given value. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.Scope(tempLower, tempUpper);
let result = range.expand(tempMiDF);
console.info("result = " + result);
// Output: result = \[30, 40\]

#### \[h2\]contains(deprecated)

contains(value: ScopeType): boolean

Checks whether a value is within this **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/ovuGFMSqT4qGNO6icezmfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FECEEE66BDC885AD4D0CB81DA5CEBC97887EB0E1C1A72EB8D341A8EE514F127C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.contains9+](#contains9-1) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScopeType](#scopetype8) | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value is within this **Scope**; otherwise, **false** is returned. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.Scope(tempLower, tempUpper);
let result = range.contains(tempMiDF);
console.info("result = " + result);
// Output: result = true

#### \[h2\]contains(deprecated)

contains(range: Scope): boolean

Checks whether a range is within this **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/eE1Z9tcETCq2V8jshGJGtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD6BBEA3E11013CEF4FE513D846CA373D0C54E0553C69472650ED1E92F8D82C4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.contains9+](#contains9-2) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Scope](#scopedeprecated) | Yes | **Scope** specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the range is within this **Scope**; otherwise, **false** is returned. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let range = new util.Scope(tempLower, tempUpper);
let tempLess = new Temperature(20);
let tempMore = new Temperature(45);
let rangeSec = new util.Scope(tempLess, tempMore);
let result = range.contains(rangeSec);
console.info("result = " + result);
// Output: result = false

#### \[h2\]clamp(deprecated)

clamp(value: ScopeType): ScopeType

Limits a value to this **Scope**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/yuVvkXkfRUyjVX_t_Ftc4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC65AAC15A6DB5B29F67834C6F5BFC03030E96A030B4E49D2A28E92997E89281)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [ScopeHelper.clamp9+](#clamp9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ScopeType](#scopetype8) | Yes | Value specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ScopeType](#scopetype8) | Returns **lowerObj** if the specified value is less than the lower limit; returns **upperObj** if the specified value is greater than the upper limit; returns the specified value if it is within this **Scope**. |

**Example**

class Temperature implements util.ScopeComparable {
  private readonly \_temp: number;

  constructor(value: number) {
    this.\_temp = value;
  }

  compareTo(value: Temperature) {
    return this.\_temp >= value.getTemp();
  }

  getTemp() {
    return this.\_temp;
  }

  toString(): string {
    return this.\_temp.toString();
  }
}

let tempLower = new Temperature(30);
let tempUpper = new Temperature(40);
let tempMiDF = new Temperature(35);
let range = new util.Scope(tempLower, tempUpper);
let result = range.clamp(tempMiDF);
console.info("result = " + result);
// Output: result = 35

#### Base64(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/vZfRu63ySYS5lyhoCP52ng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EBE459EE2FC936093D02DA89ECCDA94D5E07A513A9066192DAF2BE4D2749DAE)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper9+](#base64helper9) instead.

#### \[h2\]constructor(deprecated)

constructor()

A constructor used to create a **Base64** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/8TBXpaR0QXabRidItcm5PA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D65F4C144D48A574528027605112376771317C4326A20E3301C3636020B7299)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper.constructor9+](#constructor9-5) instead.

**System capability**: SystemCapability.Utils.Lang

**Example**

let base64 = new  util.Base64();

#### \[h2\]encodeSync(deprecated)

encodeSync(src: Uint8Array): Uint8Array

Performs Base64 encoding on the input Uint8Array byte array and returns the encoded Uint8Array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ooKzHMFsT4GqAqCe89blJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4150833A04569D228B66E299B5769BE562A6631242E654858A1184A9FE502CF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper.encodeSync9+](#encodesync9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Uint8Array object obtained. |

**Example**

let base64 = new util.Base64();
let array = new Uint8Array(\[115,49,51\]);
let result = base64.encodeSync(array);
console.info("result = " + result);
// Output: result = 99,122,69,122

#### \[h2\]encodeToStringSync(deprecated)

encodeToStringSync(src: Uint8Array): string

Performs Base64 encoding on the input Uint8Array byte array and returns the encoded string.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/LwVBPEerQIOAYeP64tnCBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B900E6BC3B79D749CD9607991F65505929D0F68BFF9BC7BCE4A140AD97449C8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper.encodeToStringSync9+](#encodetostringsync9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String obtained. |

**Example**

let base64 = new util.Base64();
let array = new Uint8Array(\[115,49,51\]);
let result = base64.encodeToStringSync(array);
console.info("result = " + result);
// Output: result = czEz

#### \[h2\]decodeSync(deprecated)

decodeSync(src: Uint8Array | string): Uint8Array

Decodes input parameters and outputs the corresponding text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/HrlQUWuGRF-7jzwWpCZbng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53CDE00FFB441C8B22E47128B7B5050CF43637B211F762500C49DDD781AB233B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper.decodeSync9+](#decodesync9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | string | Yes | Uint8Array object or string to decode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Uint8Array object obtained. |

**Example**

let base64 = new util.Base64();
let buff = 'czEz';
let result = base64.decodeSync(buff);
console.info("result = " + result);
// Output: result = 115,49,51

#### \[h2\]encode(deprecated)

encode(src: Uint8Array): Promise<Uint8Array>

Encodes the input parameter asynchronously and outputs the corresponding text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Cmp3ApZtShKObWYATCzK-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1534BBA47D83153A96572BFB9A51414AF5C5C601A6C1AF7B1C35312ACD248737)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper.encode9+](#encode9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the Uint8Array object obtained. |

**Example**

let base64 = new util.Base64();
let array = new Uint8Array(\[115,49,51\]);
base64.encode(array).then((val) => {
  console.info(val.toString());
  // Output: 99,122,69,122
})

#### \[h2\]encodeToString(deprecated)

encodeToString(src: Uint8Array): Promise<string>

Encodes the input parameter asynchronously and outputs the corresponding text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/WpeHBixHRji7kB6gf-cdIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=006324462DB001D6B22F115F754255D3DDEEBDF6D54E5CC68A19126A3ED6D360)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper.encodeToString9+](#encodetostring9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | Yes | Uint8Array object to encode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the string obtained. |

**Example**

let base64 = new util.Base64();
let array = new Uint8Array(\[115,49,51\]);
base64.encodeToString(array).then((val) => {
    console.info(val);
    // Output: czEz
})

#### \[h2\]decode(deprecated)

decode(src: Uint8Array | string): Promise<Uint8Array>

Decodes the input content into a Uint8Array object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/2cnjUQeTQJi7CA4Vs-vQsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8ADC765DD3322092554C1AC79455AB05F25E1CAAD31F9B8EA21B9B5283660BA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Base64Helper.decode9+](#decode9) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | Uint8Array | string | Yes | Uint8Array object or string to decode. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the Uint8Array object obtained. |

**Example**

let base64 = new util.Base64();
let array = new Uint8Array(\[99,122,69,122\]);
base64.decode(array).then((val) => {
  console.info(val.toString());
  // Output: 115,49,51
})
