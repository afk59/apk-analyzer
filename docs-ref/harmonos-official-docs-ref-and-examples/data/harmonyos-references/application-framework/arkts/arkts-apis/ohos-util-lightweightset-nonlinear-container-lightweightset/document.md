# @ohos.util.LightWeightSet (Nonlinear Container LightWeightSet)

LightWeightSet stores a set of values, each of which must be unique.

LightWeightSet is based on generics and uses a lightweight structure. Its default initial capacity is 8, and it has the capacity doubled in each expansion.

The values in such a set are searched using hash values, which are stored in an array.

Compared with [HashSet](../ohos-util-hashset-nonlinear-container-hashset/document.md), which can also store values, LightWeightSet occupies less memory.

**Recommended use case**: Use LightWeightSet when you need a set that has only unique elements or need to deduplicate a set.

This topic uses the following to identify the use of generics:

-   T: Type

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/WAT_pAKsSUaz3UXQBv2u0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E675DD16360030983E47FC5BA638B5ACC67B0B55C578E95B37FA5915E642D3EC)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

Container classes, implemented in static languages, have restrictions on storage locations and properties, and do not support custom properties or methods.

#### Specifications

If the value stored in **LightWeightSet** is of the number type and the value is greater than **INT32\_MAX** or less than **INT32\_MIN**, the operation result of **LightWeightSet** may be different from the expected result.

This is because the storage structure changes in such cases.

For example, **1758783600000** is greater than **INT32\_MAX** and is stored as **TaggedDouble**; **1758783600** is less than **INT32\_MIN** and is stored as **TaggedInt**. Due to these differences in storage modes, the hash algorithm will generate different hash values, leading to inconsistent mapping results and ultimately causing discrepancies from expected outcomes.

let st = new LightWeightSet<number>();
let value = 1758783600000 / 1000;  // 1758783600000 > INT32\_MAX
st.add(value);
console.info("result:", st.has(1758783600));  // result: false
console.info("result:", st.has(value));  // result: true

#### Modules to Import

import { LightWeightSet } from '@kit.ArkTS';

#### LightWeightSet

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Number of elements in a LightWeightSet. |

#### \[h2\]constructor

constructor()

A constructor used to create a **LightWeightSet** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200012 | The LightWeightSet's constructor cannot be directly invoked. |

**Example**

let lightWeightSet = new LightWeightSet<number | string>();

#### \[h2\]isEmpty

isEmpty(): boolean

Checks whether this LightWeightSet is empty (contains no element).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the LightWeightSet is empty; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The isEmpty method cannot be bound. |

**Example**

const lightWeightSet = new LightWeightSet<number>();
let result = lightWeightSet.isEmpty();
console.info("result:", result);  // result: true

#### \[h2\]add

add(obj: T): boolean

Adds an element to this LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | T | Yes | Target element. |

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

let lightWeightSet = new LightWeightSet<string>();
let result = lightWeightSet.add("squirrel");
console.info("result:", result);  // result: true

#### \[h2\]addAll

addAll(set: LightWeightSet<T>): boolean

Adds all elements in a LightWeightSet to this LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| set | LightWeightSet<T> | Yes | LightWeightSet whose elements are to be added to the current LightWeightSet. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Operation result. The value **true** is returned if the element is added; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The addAll method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let set = new LightWeightSet<string>();
set.add("gull");
lightWeightSet.addAll(set);
let result = lightWeightSet.has("gull");
console.info("result:", result);  // result: true

#### \[h2\]hasAll

hasAll(set: LightWeightSet<T>): boolean

Checks whether this LightWeightSet contains all elements of the specified LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| set | LightWeightSet<T> | Yes | **LightWeightSet** instance to be used for comparison. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if all the elements in the specified LightWeightSet are contained; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The hasAll method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let set = new LightWeightSet<string>();
set.add("sparrow");
let result = lightWeightSet.hasAll(set);
console.info("result:", result);  // result: true

#### \[h2\]has

has(key: T): boolean

Checks whether this LightWeightSet has the specified key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | T | Yes | Target key. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the specified key is contained; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The has method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<number>();
lightWeightSet.add(123);
let result = lightWeightSet.has(123);
console.info("result:", result);  // result: true

#### \[h2\]increaseCapacityTo

increaseCapacityTo(minimumCapacity: number): void

Increases the capacity of this LightWeightSet. If the passed-in capacity is greater than or equal to the number of elements in this LightWeightSet, the capacity is changed to the new capacity. If the passed-in capacity is less than the number of elements in this LightWeightSet, the capacity is not changed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| minimumCapacity | number | Yes | Minimum number of elements to accommodate in this LightWeightSet. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200001 | The value of minimumCapacity is out of range. |
| 10200011 | The increaseCapacityTo method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.increaseCapacityTo(10);

#### \[h2\]getIndexOf

getIndexOf(key: T): number

Obtains the position index of the element with the specified key in this LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | T | Yes | Key of the target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Position index of the element. If the element does not exist, a negative value is returned. The negative value consists of a minus sign and the position where the element (if available) should be. The position starts from 1. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The getIndexOf method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.getIndexOf("sparrow");
console.info("result:", result);  // result: 0

#### \[h2\]remove

remove(key: T): T

Removes an element of the specified key from this LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | T | Yes | Key of the target element. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Value of the element removed. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The remove method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.remove("sparrow");
console.info("result:", result);  // result: sparrow

#### \[h2\]removeAt

removeAt(index: number): boolean

Removes the element at the specified position from this LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Position index of the element. Must be less than or equal to INT32\_MAX, which is 2147483647. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Operation result. The value **true** is returned if the element is removed; otherwise, **false** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The removeAt method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.removeAt(1);
console.info("result:", result);  // result: true

#### \[h2\]getValueAt

getValueAt(index: number): T

Obtains the value of the element at the specified position in this LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Position index of the element. Must be less than or equal to INT32\_MAX, which is 2147483647. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Value obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The getValueAt method cannot be bound. |

**Parameters**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.getValueAt(1);
console.info("result:", result);  // result: squirrel

#### \[h2\]clear

clear(): void

Clears this LightWeightSet and sets its length to **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The clear method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
lightWeightSet.clear();
let result = lightWeightSet.isEmpty();
console.info("result:", result);  // result: true

#### \[h2\]toString

toString(): String

Obtains a string that contains all elements in this LightWeightSet.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| String | String obtained. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.toString();
console.info("result:", result);  // result: sparrow,squirrel

#### \[h2\]toArray

toArray(): Array<T>

Obtains an array that contains all objects in this LightWeightSet.

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
| 10200011 | The toArray method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let result = lightWeightSet.toArray();

#### \[h2\]values

values(): IterableIterator<T>

Returns an iterator that contains all the values in this LightWeightSet.

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

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let values = lightWeightSet.values();
for (let value of values) {
  console.info("value:", value);
}
// value: sparrow
// value: squirrel

#### \[h2\]forEach

forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet<T>) => void, thisArg?: Object): void

Uses a callback to traverse the elements in this LightWeightSet and obtain their position indexes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callbackFn | function | Yes | Callback invoked to traverse the elements in the LightWeightSet. |
| thisArg | Object | No | Value of **this** to use when **callbackFn** is invoked. The default value is this instance. |

callbackFn parameters

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | T | No | Value of the element that is currently traversed. The default value is the value of the first key-value pair. |
| key | T | No | Key of the element that is currently traversed (same as **value**). The default value is the key of the first key-value pair. |
| set | LightWeightSet<T> | No | Instance that calls the **forEach** API. The default value is this instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200011 | The forEach method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("sparrow");
lightWeightSet.add("gull");
lightWeightSet.forEach((value: string, key: string) => {
  console.info("value:" + value, "key:" + key);
});
// value:gull key:gull
// value:sparrow key:sparrow

// You are not advised to use the add, remove, or removeAt APIs in forEach because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightSet = new LightWeightSet<string>();
for(let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for(let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}

#### \[h2\]entries

entries(): IterableIterator<\[T, T\]>

Returns an iterator that contains all the elements in this LightWeightSet.

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

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let iter = lightWeightSet.entries();
for (let item of iter) {
  console.info("value:", item\[1\])
}
// value: sparrow
// value: squirrel

// You are not advised to use the add, remove, or removeAt APIs in entries because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightSet = new LightWeightSet<string>();
for(let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for(let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}

#### \[h2\]\[Symbol.iterator\]

\[Symbol.iterator\](): IterableIterator<T>

Returns an iterator. Each item of the iterator is a JavaScript object.

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

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");

// Method 1:
for (let value of lightWeightSet) {
  console.info("value:", value);
}
// value: sparrow
// value: squirrel

// Method 2:
let iter = lightWeightSet\[Symbol.iterator\]();
let temp: IteratorResult<string> = iter.next();
while(!temp.done) {
  console.info("value:", temp.value);
  temp = iter.next();
}
// value: sparrow
// value: squirrel

// You are not advised to use the add, remove, or removeAt APIs in Symbol.iterator because they may cause unpredictable risks such as infinite loops. You can use the for loop when inserting or deleting data.
let lightWeightSet = new LightWeightSet<string>();
for(let i = 0; i < 10; i++) {
  lightWeightSet.add(i + "123");
}
for(let i = 0; i < 10; i++) {
  lightWeightSet.remove(i + "123");
}

#### \[h2\]equal(deprecated)

equal(obj: Object): boolean

Checks whether the elements of this LightWeightSet are the same as those of **obj**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/WrbQt-h7SC-KbkvPuJahYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062224Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C57A0F54208E7D18516403CB8D300D6EDE215F371A28D55D9C6B51BE6102A228)

This API is supported since API version 8 and deprecated since API version 12. There is no substitute API.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | Object | Yes | **LightWeightSet** instance to be used for comparison. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if **obj** is a LightWeightSet or an array containing only strings or numbers and the elements in them are the same; returns **false** in other cases. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200011 | The equal method cannot be bound. |

**Example**

let lightWeightSet = new LightWeightSet<string>();
lightWeightSet.add("squirrel");
lightWeightSet.add("sparrow");
let obj = \["sparrow", "squirrel"\];
let result = lightWeightSet.equal(obj);
console.info("result:", result);  // result: true
