# @ohos.util.Deque (Linear Container Deque)

Double-Ended Queue (Deque) is a data structure implemented based on a circular queue. It supports insertion and deletion of elements at both ends. It follows the principles of First In First Out (FIFO) and Last In First Out (LIFO). Deque can dynamically adjust the capacity based on project requirements. It doubles the capacity each time.

Queue allows element removal at the front and insertion at the rear. Compared with [Queue](../ohos-util-queue-linear-container-queue/document.md), which only allows element deletion at the front and insertion at the back, Deque permits insertion and deletion at both ends.

Both [ArrayList](../ohos-util-arraylist-linear-container-arraylist/document.md) and Deque support insertion and deletion at the ends, but Deque does not support insertion in the middle. Deque is more efficient than an ArrayList for inserting and deleting elements at the front, whereas an ArrayList excels in element access efficiency.

**Recommended use case**: Use **Deque** when you need to frequently insert or remove elements at both the ends of a container.

This topic uses the following to identify the use of generics:

-   T: Type

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/S_dbqwLMR-SBP70d6k4Qxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5407D0721C96BEC4522C633449A6FAE63989AFCA91FB9220D3D1760C2E662B46)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Container classes, implemented in static languages, have restrictions on storage locations and properties, and do not support custom properties or methods.
    

#### Modules to Import

import { Deque } from '@kit.ArkTS';

#### Deque

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Number of elements in a Deque. |

#### \[h2\]constructor

constructor()

A constructor used to create a **Deque** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200012 | The Deque's constructor cannot be directly invoked. |

**Example**

let deque = new Deque<string | number | boolean | Object>();

#### \[h2\]insertFront

insertFront(element: T): void

Inserts an element at the front of this Deque.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The insertFront method cannot be bound. |

**Example**

class C1 {
  name: string = ""
  age: string = ""
}

let deque = new Deque<string | number | boolean | Array<number> | C1>();
deque.insertFront("a");
deque.insertFront(1);
let b = \[1, 2, 3\];
deque.insertFront(b);
let c: C1 = {name : "Dylan", age : "13"};
deque.insertFront(c);
deque.insertFront(false);
console.info("result:", deque\[0\]);  // result: false

#### \[h2\]insertEnd

insertEnd(element: T): void

Inserts an element at the end of this Deque.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The insertEnd method cannot be bound. |

**Example**

class C1 {
  name: string = ""
  age: string = ""
}

let deque = new Deque<string | number | boolean | Array<number> | C1>();
deque.insertEnd("a");
deque.insertEnd(1);
let b = \[1, 2, 3\];
deque.insertEnd(b);
let c: C1 = {name : "Dylan", age : "13"};
deque.insertEnd(c);
deque.insertEnd(false);
console.info("result:", deque\[0\]);  // result: a

#### \[h2\]has

has(element: T): boolean

Checks whether this Deque has the specified element.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Operation result. The value **true** is returned if the specified element is contained; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The has method cannot be bound. |

**Example**

let deque = new Deque<string>();
deque.insertFront("squirrel");
let result = deque.has("squirrel");
console.info("result:", result);  // result: true

#### \[h2\]popFirst

popFirst(): T

Removes the first element of this Deque.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | First element removed. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The popFirst method cannot be bound. |

**Example**

let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertEnd(5);
deque.insertFront(2);
deque.insertFront(4);
let result = deque.popFirst();
console.info("result:", result);  // result: 4

#### \[h2\]popLast

popLast(): T

Removes the last element of this Deque.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | Last element removed. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The popLast method cannot be bound. |

**Example**

let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(6);
deque.insertFront(5);
deque.insertFront(2);
deque.insertFront(4);
let result = deque.popLast();
console.info("result:", result);  // result: 6

#### \[h2\]forEach

forEach(callbackFn: (value: T, index?: number, deque?: Deque<T>) => void, thisArg?: Object): void

Uses a callback to traverse each element in the **Deque** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked to traverse the elements in the Deque. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this instance. |

callbackFn parameters

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Value of the element that is currently traversed. |
| index | number | No | Position index of the element that is currently traversed. The default value is **0**. |
| deque | Deque<T> | No | Instance that calls the **forEach** API. The default value is this instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**Example**

let deque = new Deque<number>();
deque.insertFront(2);
deque.insertEnd(3);
deque.insertFront(1);
deque.insertEnd(4);
deque.forEach((value: number, index: number): void => {
  console.info("value:" + value, "index:" + index);
});
/\*
Output: value:1 index:0
        value:2 index:1
        value:3 index:2
        value:4 index:3
\*/

#### \[h2\]getFirst

getFirst(): T

Obtains the first element of this Deque.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | First element of the T type obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getFirst method cannot be bound. |

**Example**

let deque = new Deque<number>();
deque.insertEnd(2);
deque.insertEnd(4);
deque.insertFront(5);
deque.insertFront(4);
let result = deque.getFirst();
console.info("result:", result);  // result: 4

#### \[h2\]getLast

getLast(): T

Obtains the last element of this Deque.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | Last element of the T type obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getLast method cannot be bound. |

**Example**

let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);
let result = deque.getLast();
console.info("result:", result);  // result: 2

#### \[h2\]\[Symbol.iterator\]

\[Symbol.iterator\](): IterableIterator<T>

Returns an iterator, each item of which is a JavaScript object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<T> | Iterator obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**Example**

let deque = new Deque<number>();
deque.insertFront(2);
deque.insertFront(4);
deque.insertFront(5);
deque.insertFront(4);

// Method 1:
for (let item of deque) {
  console.info("value:" + item);
}
/\*
Output: 4
        5
        4
        2
\*/

// Method 2:
let iter = deque\[Symbol.iterator\]();
let temp:IteratorResult<number> = iter.next();
while(!temp.done) {
  console.info("value:" + temp.value);
  temp = iter.next();
}
/\*
Output: 4
        5
        4
        2
\*/
