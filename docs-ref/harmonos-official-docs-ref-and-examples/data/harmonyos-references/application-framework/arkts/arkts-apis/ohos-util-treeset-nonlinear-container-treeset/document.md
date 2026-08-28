# @ohos.util.TreeSet (Nonlinear Container TreeSet)

TreeSet is implemented based on [TreeMap](../ohos-util-treemap-nonlinear-container-treemap/document.md). In TreeSet, only **value** objects are processed. TreeSet can be used to store values, each of which must be unique.

TreeSet and [HashSet](../ohos-util-hashset-nonlinear-container-hashset/document.md) do not allow duplicate elements. Data in a HashSet is stored in an unordered manner, whereas elements in a TreeSet are stored in a sorted order. HashSet permits the insertion of null values. However, you are not advised to insert null into a TreeSet, as it may affect the sorting results.

Recommended use case: Use TreeSet when you need to store data in sorted order.

This topic uses the following to identify the use of generics:

-   T: Type

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/YF9dp4-sTn69Z2wy0PgHCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEF45F36D98A56F9548D497B5EAE17B033F005A177C869A61F92F0C17A1C6F03)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

Container classes, implemented in static languages, have restrictions on storage locations and properties, and do not support custom properties or methods.

#### Modules to Import

import { TreeSet } from '@kit.ArkTS';

#### TreeSet

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Number of elements in a TreeSet. |

#### \[h2\]constructor

constructor(comparator?: (firstValue: T, secondValue: T) => boolean)

A constructor used to create a **TreeSet** instance. It supports sorting elements in ascending or descending order by using comparators.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| comparator | function | No | Custom comparator, which can be used to sort elements based on the comparison relationship. The default value is null, indicating that no comparator is provided. |

comparator parameters

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| firstValue | T | Yes | Previous element. |
| secondValue | T | Yes | Next element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200012 | The TreeSet's constructor cannot be directly invoked. |

**Example**

// Default constructor.
let treeSet = new TreeSet<string | number | boolean | Object>();

// Use the comparator firstValue < secondValue if the elements are expected to be sorted in ascending order. Use firstValue > secondValue if the elements are expected to be sorted in descending order.
let treeSet: TreeSet<string> = new TreeSet<string>((firstValue: string, secondValue: string): boolean => {
  return firstValue < secondValue;
});
treeSet.add("a");
treeSet.add("c");
treeSet.add("d");
treeSet.add("b");
for (let value of treeSet) {
  console.info("value:", value);
}
// value: a
// value: b
// value: c
// value: d

// When a custom type is inserted, a comparator must be provided.
class TestEntry{
  public id: number = 0;
}
let ts1: TreeSet<TestEntry> = new TreeSet<TestEntry>((t1: TestEntry, t2: TestEntry): boolean => {return t1.id > t2.id;});
let entry1: TestEntry = {
  id: 0
};
let entry2: TestEntry = {
  id: 1
}
ts1.add(entry1);
ts1.add(entry2);
console.info("treeSet: ", ts1.length);

#### \[h2\]isEmpty

isEmpty(): boolean

Checks whether this TreeSet is empty (contains no element).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the TreeSet is empty; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The isEmpty method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
let result = treeSet.isEmpty();
console.info("result:", result);  // result: true

#### \[h2\]has

has(value: T): boolean

Checks whether this TreeSet has the specified value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Target value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the specified value is contained; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The has method cannot be bound. |

**Example**

let treeSet  = new TreeSet<number>();
treeSet.add(123);
let result = treeSet.has(123);
console.info("result:", result); // result: true

#### \[h2\]getFirstValue

getFirstValue(): T

Obtains the value of the first element in this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | Value obtained. If nothing is obtained, **undefined** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getFirstValue method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.getFirstValue();
console.info("result:", result); // result: sparrow

#### \[h2\]getLastValue

getLastValue(): T

Obtains the value of the last element in this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | Value obtained. If nothing is obtained, **undefined** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getLastValue method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.getLastValue();
console.info("result:", result); // result: squirrel

#### \[h2\]add

add(value: T): boolean

Adds an element to this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the element is added successfully; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The add method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
let result = treeSet.add("squirrel");
console.info("result:", result); // result: true

#### \[h2\]remove

remove(value: T): boolean

Removes the element with the specified key from this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Key of the target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the element is removed successfully; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The remove method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.remove("sparrow");
console.info("result:", result); // result: true

#### \[h2\]getLowerValue

getLowerValue(key: T): T

Obtains the value that is placed in front of the input key in this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | T | Yes | Input key. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Value obtained. If nothing is obtained, **undefined** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The getLowerValue method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
treeSet.add("gander");
let result = treeSet.getLowerValue("sparrow");
console.info("result:", result); // result: gander

#### \[h2\]getHigherValue

getHigherValue(key: T): T

Obtains the value that is placed next to the input key in this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | T | Yes | Input key. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Value obtained. If nothing is obtained, **undefined** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200011 | The getHigherValue method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
treeSet.add("gander");
let result = treeSet.getHigherValue("sparrow");
console.info("result:", result); // result: squirrel

#### \[h2\]popFirst

popFirst(): T

Removes the first element in this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | Element removed. If nothing is obtained, **undefined** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The popFirst method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.popFirst();
console.info("result:", result); // result: sparrow

#### \[h2\]popLast

popLast(): T

Removes the last element in this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| T | Element removed. If nothing is obtained, **undefined** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The popLast method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let result = treeSet.popLast();
console.info("result:", result); // result: squirrel

#### \[h2\]clear

clear(): void

Clears this TreeSet and sets its length to **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The clear method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
treeSet.clear();
let result = treeSet.isEmpty();
console.info("result:", result); // result: true

#### \[h2\]values

values(): IterableIterator<T>

Returns an iterator that contains all the values in this TreeSet.

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
| 10200011 | The values method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let values = treeSet.values();
for (let value of values) {
  console.info("value:", value)
}
// value: sparrow
// value: squirrel

#### \[h2\]forEach

forEach(callbackFn: (value?: T, key?: T, set?: TreeSet<T>) => void, thisArg?: Object): void

Uses a callback to traverse the elements in this TreeSet and obtain their indexes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked to traverse the elements in the TreeSet. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this instance. |

callbackFn

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | No | Value of the element that is currently traversed. |
| key | T | No | Key of the element that is currently traversed. |
| set | TreeSet<T> | No | Instance that calls the **forEach** API. The default value is this instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("sparrow");
treeSet.add("gull");
treeSet.forEach((value: string, key: string): void => {
  console.info("value:" + value);
});
// value:gull
// value:sparrow

// You are not advised to use the set or remove APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let treeSet = new TreeSet<string>();
for(let i = 0; i < 10; i++) {
  treeSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  treeSet.remove("sparrow" + i);
}

#### \[h2\]entries

entries(): IterableIterator<\[T, T\]>

Returns an iterator that contains all the elements in this TreeSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[T, T\]> | Iterator obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The entries method cannot be bound. |

**Example**

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
let it = treeSet.entries();
let t: IteratorResult<Object\[\]> = it.next();
while(!t.done) {
  console.info("TreeSet: " + t.value\[1\]);
  t = it.next()
}
// TreeSet: sparrow
// TreeSet: squirrel

// You are not advised to use the set or remove APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let treeSet = new TreeSet<string>();
for(let i = 0; i < 10; i++) {
  treeSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  treeSet.remove("sparrow" + i);
}

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

let treeSet = new TreeSet<string>();
treeSet.add("squirrel");
treeSet.add("sparrow");
// Method 1:
for (let item of treeSet) {
  console.info("value:" + item);
}
// value:sparrow
// value:squirrel

// Method 2:
let iter = treeSet\[Symbol.iterator\]();
let temp: IteratorResult<string> = iter.next().value;
while(temp != undefined) {
  console.info("value:" + temp);
  temp = iter.next().value;
}
// value:sparrow
// value:squirrel

// You are not advised to use the set or remove APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let treeSet = new TreeSet<string>();
for(let i = 0; i < 10; i++) {
  treeSet.add("sparrow" + i);
}
for(let i = 0; i < 10; i++) {
  treeSet.remove("sparrow" + i);
}
