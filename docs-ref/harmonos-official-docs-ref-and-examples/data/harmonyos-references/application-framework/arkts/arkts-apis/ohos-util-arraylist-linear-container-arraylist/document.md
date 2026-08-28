# @ohos.util.ArrayList (Linear Container ArrayList)

ArrayList is a linear data structure that is implemented based on arrays. ArrayList can dynamically adjust the capacity based on project requirements. It increases the capacity by 50% each time.

When compared with [LinkedList](../ohos-util-linkedlist-linear-container-linkedlist/document.md), ArrayList is more efficient in random access but less efficient in the addition or removal operation, because its addition or removal operation affects the position of other elements in the container.

**Recommended use case**: Use ArrayList when elements in a container need to be frequently read.

This topic uses the following to identify the use of generics:

-   T: Type

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/6fgAGWWaQdCqjoFr9uIYFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E601D3FC9A01CF425273617CC1A9DC79191F6399F6FC99D980361A69E112664F)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   Container classes, implemented in static languages, have restrictions on storage locations and properties, and do not support custom properties or methods.
    

#### Modules to Import

import { ArrayList } from '@kit.ArkTS';

#### ArrayList

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Number of elements in an ArrayList. |

#### \[h2\]constructor

constructor()

A constructor used to create an **ArrayList** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200012 | The ArrayList's constructor cannot be directly invoked. |

**Example**

let arrayList = new ArrayList<string | number>();

#### \[h2\]add

add(element: T): boolean

Adds an element at the end of this ArrayList.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Operation result. The value **true** is returned if the element is added; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The add method cannot be bound. |

**Example**

class C1 {
  name: string = ""
  age: string = ""
}
let arrayList = new ArrayList<string | number | boolean | Array<number> | C1>();
arrayList.add("a");
arrayList.add(1);
let b = \[1, 2, 3\];
arrayList.add(b);
let c : C1 = {name: "Dylan", age: "13"}
let result1 = arrayList.add(c);
let result2 = arrayList.add(false);
console.info("result1:", result1);  // result1: true
console.info("result2:", result2);  // result2: true
console.info("length:", arrayList.length);  // length: 5

#### \[h2\]insert

insert(element: T, index: number): void

Inserts an element at a specified index within the length range. If index is out of range, the insertion fails.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |
| index | number | Yes | Index of the position where the element is to be inserted. The value must be less than or equal to int32\_max, that is, 2147483647. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of index is out of range. |
| 10200011 | The insert method cannot be bound. |

**Example**

let arrayList = new ArrayList<number | string | boolean>();
arrayList.insert("A", 0);
arrayList.insert(0, 1);
arrayList.insert(true, 2);
console.info("length:", arrayList.length);  // length: 3

#### \[h2\]has

has(element: T): boolean

Checks whether this ArrayList has the specified element.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the specified element is contained; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The has method cannot be bound. |

**Example**

let arrayList = new ArrayList<string>();
arrayList.add("squirrel");
let result: boolean = arrayList.has("squirrel");
console.info("result:", result);  // result: true

#### \[h2\]getIndexOf

getIndexOf(element: T): number

Obtains the index of the first occurrence of the specified element in this ArrayList.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns the position index if obtained; returns **\-1** if the specified element is not found. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getIndexOf method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.getIndexOf(2);
console.info("result = ", result); // result = 0

#### \[h2\]getLastIndexOf

getLastIndexOf(element: T): number

Obtains the index of the last occurrence of the specified element in this ArrayList.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns the position index if obtained; returns **\-1** if the specified element is not found. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getLastIndexOf method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(1);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.getLastIndexOf(2);
console.info("result = ", result); // result = 5

#### \[h2\]removeByIndex

removeByIndex(index: number): T

Removes an element with the specified position from this ArrayList.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Position index of the target element. The value must be less than or equal to int32\_max, that is, 2147483647. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Element removed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of "index" is out of range. |
| 10200011 | The removeByIndex method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(2);
arrayList.add(4);
let result: number = arrayList.removeByIndex(2);
console.info("result = ", result); // result = 5

#### \[h2\]remove

remove(element: T): boolean

Removes the first occurrence of the specified element from this ArrayList.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| element | T | Yes | Target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Operation result. The value **true** is returned if the element is removed; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The remove method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.remove(2);
console.info("result = ", result); // result =  true

#### \[h2\]removeByRange

removeByRange(fromIndex: number, toIndex: number): void

Removes elements within the range \[fromIndex, toIndex).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fromIndex | number | Yes | Index of the start position. |
| toIndex | number | Yes | Index of the end position. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The removeByRange method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.removeByRange(2, 4);

#### \[h2\]replaceAllElements

replaceAllElements(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => T, thisArg?: Object): void

Replaces all elements in this ArrayList with new elements, and returns the new ones.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked for the replacement. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this instance. |

callbackFn parameters

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Value of the element that is currently traversed. |
| index | number | No | Position index of the element that is currently traversed. The default value is **0**. |
| arrlist | ArrayList<T> | No | Instance that calls the **replaceAllElements** API. The default value is this instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The replaceAllElements method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.replaceAllElements((value: number): number => {
  // Add the user operation logic based on the actual scenario.
  return value;
});

#### \[h2\]forEach

forEach(callbackFn: (value: T, index?: number, arrlist?: ArrayList<T>) => void, thisArg?: Object): void

Uses a callback to traverse each element in the **ArrayList** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked for the replacement. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this instance. |

callbackFn parameters

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Value of the element that is currently traversed. |
| index | number | No | Position index of the element that is currently traversed. The default value is **0**. |
| arrlist | ArrayList<T> | No | Instance that calls the **forEach** API. The default value is this instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.forEach((value: number, index?: number) => {
  console.info("value:" + value, "index:" + index);
});
// value:2 index:0
// value:4 index:1
// value:5 index:2
// value:4 index:3

#### \[h2\]sort

sort(comparator?: (firstValue: T, secondValue: T) => number): void

Sorts elements in an ArrayList according to the order defined by the specified comparator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| comparator | function | No | Callback invoked for sorting. The default value is the callback function for sorting elements in ascending order. |

comparator

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| firstValue | T | Yes | Previous element. |
| secondValue | T | Yes | Next element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 10200011 | The sort method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.sort((a: number, b: number) => a - b);
arrayList.sort((a: number, b: number) => b - a);
arrayList.sort();

#### \[h2\]subArrayList

subArrayList(fromIndex: number, toIndex: number): ArrayList<T>

Obtains elements from this **ArrayList** within the range \[fromIndex, toIndex) and returns them as a new ArrayList instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fromIndex | number | Yes | Index of the start position. |
| toIndex | number | Yes | Index of the end position. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayList<T> | New **ArrayList** instance obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of fromIndex or toIndex is out of range. |
| 10200011 | The subArrayList method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: ArrayList<number> = arrayList.subArrayList(2, 4);
console.info("result = ", result.length); // result = 2

#### \[h2\]clear

clear(): void

Clears this ArrayList and sets its length to **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The clear method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.clear();

#### \[h2\]clone

clone(): ArrayList<T>

Clones this ArrayList and returns a copy. The modification to the copy does not affect the original instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayList<T> | New **ArrayList** instance obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The clone method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result:  ArrayList<number> = arrayList.clone();
console.info("result = ", result.length); // result = 4

#### \[h2\]getCapacity

getCapacity(): number

Obtains the capacity of this ArrayList.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Capacity obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getCapacity method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: number = arrayList.getCapacity();
console.info("result = ", result); // result = 10

#### \[h2\]convertToArray

convertToArray(): Array<T>

Converts this ArrayList into an array.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| Array<T> | Array obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The convertToArray method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: Array<number> = arrayList.convertToArray();
console.info("result = ", result); // result =  2,4,5,4

#### \[h2\]isEmpty

isEmpty(): boolean

Checks whether this ArrayList is empty (contains no element).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the ArrayList is empty; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The isEmpty method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: boolean = arrayList.isEmpty();
console.info("result = ", result); // result =  false

#### \[h2\]\[index: number\]12+

\[index: number\]: T

Returns the element at the given index.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index. The value must be less than or equal to int32\_max, that is, 2147483647. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Element obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 10200001 | The value of index is out of range. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
let result: number = arrayList\[2\];
console.info("result = ", result); // result =  5

#### \[h2\]increaseCapacityTo

increaseCapacityTo(newCapacity: number): void

Increases the capacity of this ArrayList.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| newCapacity | number | Yes | New capacity. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The increaseCapacityTo method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.increaseCapacityTo(2);
arrayList.increaseCapacityTo(8);
console.info("result = ", arrayList.length); // result = 4

#### \[h2\]trimToCurrentLength

trimToCurrentLength(): void

Releases the reserved space in this ArrayList by adjusting the capacity to the actual number of elements in it.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The trimToCurrentLength method cannot be bound. |

**Example**

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);
arrayList.trimToCurrentLength();
console.info("result = ", arrayList.length); // result = 4

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

let arrayList = new ArrayList<number>();
arrayList.add(2);
arrayList.add(4);
arrayList.add(5);
arrayList.add(4);

// Method 1:
for (let value of arrayList) {
  console.info("value:", value);
}
// value: 2
// value: 4
// value: 5
// value: 4

// Method 2:
let iter = arrayList\[Symbol.iterator\]();
let temp: IteratorResult<number> = iter.next();
while(!temp.done) {
  console.info("value:", temp.value);
  temp = iter.next();
}
// value: 2
// value: 4
// value: 5
// value: 4
