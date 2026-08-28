# @ohos.util.HashMap (Nonlinear Container HashMap)

HashMap is implemented using an array, linked lists, and red-black trees as its core, supporting efficient querying, insertion and deletion operations. It stores data as key-value pairs where duplicate keys are not allowed - each key can only map to a single value.

HashMap is faster in accessing data than [TreeMap](../ohos-util-treemap-nonlinear-container-treemap/document.md), because the former accesses the keys based on the hash codes, whereas the latter stores and accesses the keys in sorted order.

[HashSet](../ohos-util-hashset-nonlinear-container-hashset/document.md) is implemented based on HashMap. The input parameter of HashMap consists of **key** and **value**. In HashSet, only the **value** object is processed.

**Recommended use case**: Use HashMap when you need to quickly access, remove, and insert key-value pairs.

This topic uses the following to identify the use of generics:

-   K: Key
    
-   V: Value

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/fMwzOhyKQGi23nI_zVrA_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=796C1961BDF1CAD5D7789FB45668D8CE7D34BCCE642FD63E9062FAAB5738C79A)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

Container classes, implemented in static languages, have restrictions on storage locations and properties, and do not support custom properties or methods.

#### Modules to Import

import { HashMap } from '@kit.ArkTS';

#### HashMap

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Number of elements in a HashMap. |

#### \[h2\]constructor

constructor()

A constructor used to create a **HashMap** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200012 | The HashMap's constructor cannot be directly invoked. |

**Example**

let hashMap = new HashMap<string, number>();

#### \[h2\]isEmpty

isEmpty(): boolean

Checks whether this HashMap is empty (contains no element).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the HashMap is empty; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The isEmpty method cannot be bound. |

**Example**

const hashMap = new HashMap<string, number>();
let result = hashMap.isEmpty();
console.info("result = ", result) // result = true

#### \[h2\]hasKey

hasKey(key: K): boolean

Checks whether this HashMap has the specified key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Target key. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the specified key is contained; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The hasKey method cannot be bound. |

**Example**

const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
let result = hashMap.hasKey("squirrel");
console.info("result:", result);  // result: true

#### \[h2\]hasValue

hasValue(value: V): boolean

Checks whether this HashMap has the specified value.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | V | Yes | Target value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the specified value is contained; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The hasValue method cannot be bound. |

**Example**

const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
let result = hashMap.hasValue(123);
console.info("result:", result);  // result: true

#### \[h2\]get

get(key: K): V

Obtains the value of the specified key in this HashMap. If nothing is obtained, **undefined** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Target key. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | Value obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The get method cannot be bound. |

**Example**

const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let result = hashMap.get("sparrow");
console.info("result:", result);  // result: 356

#### \[h2\]setAll

setAll(map: HashMap<K, V>): void

Adds all element groups in a HashMap to another HashMap.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| map | HashMap<K, V> | Yes | HashMap for element addition. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The setAll method cannot be bound. |

**Example**

const hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let newHashMap = new HashMap<string, number>();
newHashMap.set("newMap", 99);
hashMap.setAll(newHashMap);
let result = hashMap.hasKey("newMap");
console.info("result:", result);  // result: true

#### \[h2\]set

set(key: K, value: V): Object

Adds or updates an element in this HashMap.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key of the target element. |
| value | V | Yes | Value of the target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | HashMap after addition or update. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 10200011 | The set method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123)
console.info("result:", hashMap.get("squirrel"));  // result: 123

#### \[h2\]remove

remove(key: K): V

Removes an element with the specified key from this HashMap.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key of the target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| V | Value of the element. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The remove method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let result = hashMap.remove("sparrow");
console.info("result:", result);  // result: 356

#### \[h2\]clear

clear(): void

Clears this HashMap and sets its length to **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The clear method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
hashMap.clear();
let result = hashMap.isEmpty();
console.info("result:", result);  // result: true

#### \[h2\]keys

keys(): IterableIterator<K>

Returns an iterator that contains all the keys in this HashMap.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<K> | Iterator obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The keys method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let keys = hashMap.keys();
for (let key of keys) {
  console.info("key:" + key);
}
// key:squirrel
// key:sparrow

#### \[h2\]values

values(): IterableIterator<V>

Returns an iterator that contains all the values in this HashMap.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<V> | Iterator obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The values method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let values = hashMap.values();
for (let value of values) {
  console.info("value:", value)
}
// value: 123
// value: 356

#### \[h2\]replace

replace(key: K, newValue: V): boolean

Replaces the value of a specified key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | K | Yes | Key of the target element. |
| newValue | V | Yes | New value of the element. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Operation result. The value **true** is returned if the element is replaced; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The replace method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("sparrow", 123);
let result = hashMap.replace("sparrow", 357);
console.info("result:", result);  // result: true

#### \[h2\]forEach

forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object): void

Uses a callback to traverse each element.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked to traverse the elements in the HashMap. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this instance. |

callbackFn parameters

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | V | No | Value of the element that is currently traversed. |
| key | K | No | Key of the element that is currently traversed. |
| map | HashMap<K, V> | No | Instance that calls the **forEach** API. The default value is this instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("sparrow", 123);
hashMap.set("gull", 357);
hashMap.forEach((value: number, key: string) => {
  console.info("value: " + value, "key: " + key);
});
// value: 123 key: sparrow
// value: 357 key: gull

// You are not advised to use the set or remove APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}

#### \[h2\]entries

entries(): IterableIterator<\[K, V\]>

Returns an iterator that contains all the elements in this HashMap.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[K, V\]> | Iterator obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The entries method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);
let iter = hashMap.entries();
let temp: IteratorResult<Object\[\]> = iter.next();
while(!temp.done) {
  console.info("key:" + temp.value\[0\]);
  console.info("value:" + temp.value\[1\]);
  temp = iter.next();
}

// You are not advised to use the set or remove APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}

#### \[h2\]\[Symbol.iterator\]

\[Symbol.iterator\](): IterableIterator<\[K, V\]>

Returns an iterator, each item of which is a JavaScript object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| IterableIterator<\[K, V\]> | Iterator obtained. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The Symbol.iterator method cannot be bound. |

**Example**

let hashMap = new HashMap<string, number>();
hashMap.set("squirrel", 123);
hashMap.set("sparrow", 356);

// Method 1:
for (let item of hashMap) {
  console.info("key:", item\[0\]);
  console.info("value:", item\[1\]);
}
// key: squirrel
// value: 123
// key: sparrow
// value: 356

// Method 2:
let iter = hashMap\[Symbol.iterator\]();
let temp: IteratorResult<Object\[\]> = iter.next();
while(!temp.done) {
  console.info("key:", temp.value\[0\]);
  console.info("value:", temp.value\[1\]);
  temp = iter.next();
}
// key: squirrel
// value: 123
// key: sparrow
// value: 356

// You are not advised to use the set or remove APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let hashMap = new HashMap<string, number>();
for(let i = 0; i < 10; i++) {
  hashMap.set("sparrow" + i, 123);
}

for(let i = 0; i < 10; i++) {
  hashMap.remove("sparrow" + i);
}
