# Class (Set)

A non-linear data structure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/pxkR8bv3Roiuzd8N_QOJLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062221Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9751248DBF5D8A18189D046B5F858B57DBFCA7959552922A21C6F027CA4A7FF0)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module can be imported only to ArkTS files (with the file name extension .ets).
    

This section uses the following to identify the use of generics:

-   T: type, which can be any of the [sendable data types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-data-types).

**Decorator**: @Sendable

#### Modules to Import

import { collections } from '@kit.ArkTS';

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size | number | Yes | No | Number of elements in a set. |

#### constructor

constructor(values?: readonly T\[\] | null)

A constructor used to create an ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| values | readonly T\[\] | null | No | Array or iterator object. The default value is **null**, indicating that an empty set is created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Set's constructor cannot be directly invoked. |

**Example**

// Positive example 1:
const mySet = new collections.Set<number>();

// Positive example 2:
const mySet = new collections.Set<number>(\[1, 2, 3, 4, 5\]);

// Negative example:
@Sendable
class SharedClass {
  constructor() {
  }
}

let sObj = new SharedClass();
const mySet1: collections.Set<number|SharedClass> = new collections.Set<number|SharedClass>(\[1, sObj\]);
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
let obj = new Object();
const mySet2: collections.Set<number|SharedClass> = new collections.Set<number|Object>(\[1, obj\]);

#### constructor

constructor(iterable: Iterable<T>)

A constructor used to create an ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| iterable | Iterable<T> | Yes | Object used to construct an ArkTS set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 10200012 | The ArkTS Set's constructor cannot be directly invoked. |

**Example**

const mapper = new Map(\[
  \['1', 'a'\],
  \['2', 'b'\],
\]);
let newSet = new collections.Set<string>(mapper.values());
console.info(newSet.has('a').toString()); // Expected output: true
console.info(newSet.has('b').toString()); // Expected output: true

#### entries

entries(): IterableIterator<\[T, T\]>

Returns a set iterator object that contains the key-value pair of each element in this ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[T, T\]> | Returns a set iterator object that contains the key-value pair of each element in this ArkTS set. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The entries method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

const mySet = new collections.Set<number>(\[0, 1, 2, 3\]);

const iterator = mySet.entries();
// Expected output: \[0, 0\]
console.info(iterator.next().value);
// Expected output: \[1, 1\]
console.info(iterator.next().value);

#### keys

keys(): IterableIterator<T>

Returns a set iterator object that contains the key of each element in this ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<T> | Returns a set iterator object that contains the key of each element in this ArkTS set. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The keys method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

const mySet = new collections.Set<number>(\[0, 1, 2, 3\]);

const iterator = mySet.keys();
// Expected output: 0
console.info(iterator.next().value);
// Expected output: 1
console.info(iterator.next().value);

#### values

values(): IterableIterator<T>

Returns a set iterator object that contains the value of each element in this ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<T> | Returns a set iterator object that contains the value of each element in this ArkTS set. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The values method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

// Example 1:
const mySet = new collections.Set<number>(\[0, 1, 2, 3\]);

const iterator = mySet.values();
// Expected output: 0
console.info(iterator.next().value);
// Expected output: 1
console.info(iterator.next().value);

// Example 2:
const mySet = new collections.Set<number>(\[0, 1, 2, 3\]);

const valueIter = mySet.values();
for (let value of valueIter) {
    if (value % 2 == 0) {
        mySet.delete(value);
    }
}

// Expected output: 2
console.info("size:" + mySet.size);

#### clear

clear(): void

Removes all elements from this ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The clear method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

const mySet = new collections.Set<number>(\[0, 1\]);
// Expected output: 2
console.info("size:" + mySet.size);
mySet.clear();
// Expected output: 0
console.info("size:" + mySet.size);

#### delete

delete(value: T): boolean

Deletes an element from this ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Target value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Operation result. The value **true** is returned if the key is deleted; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The delete method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

const mySet = new collections.Set<string>(\["hello", "world"\]);
// Expected result: true
console.info("result:" + mySet.delete("hello"));
// Expected result: false
console.info("result:" + mySet.has("hello"));
// Expected result: false
console.info("result:" + mySet.delete("hello"));

#### forEach

forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void

Calls a callback function for each key-value pair in this ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | (value: T, value2: T, set: Set<T>) => void | Yes | Callback function to run for each key-value pair. |

callbackFn parameters

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | No | Value of the element that is currently traversed. |
| value2 | T | No | Key of the element that is currently traversed. |
| set | Set<T> | No | Current set object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The forEach method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

// Positive example:
new collections.Set<string>(\['foo', 'bar', 'baz'\]).forEach((value1, value2, set) => {
  console.info(\`s\[${value1}\] = ${value2}\`);
});

// Negative example:
new collections.Set<string>(\['foo', 'bar', 'baz'\]).forEach((value1, value2, set) => {
  // Throw exception \`Concurrent modification error.\`
  set.delete(value1);
});

#### has

has(value: T): boolean

Checks whether a value exists in this ArkTS set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Target key. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the value exists; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The has method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

const mySet = new collections.Set<string>(\["hello", "world"\]);
// Expected output: true
console.info("result:" + mySet.has("hello"));
// Expected output: true
console.info("result:" + mySet.has("world"));

#### add

add(value: T): Set<T>

Checks whether a value exists in this ArkTS set, and if not, adds the value to the set.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | Yes | Target value. |

**Return value**

| Type | Description |
| :-- | :-- |
| Set<T> | Set object. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The add method cannot be bound with non-sendable. |
| 10200201 | Concurrent modification error. |

**Example**

// Positive example:
const mySet: collections.Set<string> = new collections.Set<string>();
mySet.add("foo");

// Negative example:
let obj = new Object();
const mySet: collections.Set<Object> = new collections.Set<Object>();
// Type arguments of generic "Sendable" type must be a "Sendable" data type (arkts-sendable-generic-types)
mySet.add(obj);

#### \[Symbol.iterator\]

\[Symbol.iterator\](): IterableIterator<T>

Returns an iterator, each item of which is a JavaScript object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Hkdx4DUdS6yMwO0oJkjNFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062221Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=702ED35E9B1EB48A7FC11F924C0BEDD2F25A782DDBE1DE0BDFB854E2BE231B45)

This API cannot be used in .ets files.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<T> | Iterator obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**Example**

let set = new collections.Set<number>(\[1, 2, 3, 4, 5\]);

let val: Array<number> = Array.from(set.values());
for (let item of val) {
  console.info("value: " + item);
}
