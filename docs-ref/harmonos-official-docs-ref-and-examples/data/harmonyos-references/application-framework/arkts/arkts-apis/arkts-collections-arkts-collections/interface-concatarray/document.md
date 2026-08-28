# Interface (ConcatArray)

An array-like object that can be concatenated. This API extends **ISendable**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/4ML-trgHStKC7wRq69pBGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F66099290AF70F97AAD3A50809F3D4C6E40E3F9B68C2A74B98FEC51BE11891A4)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module can be imported only to ArkTS files (with the file name extension .ets).
    

This section uses the following to identify the use of generics:

-   T: type, which can be any of the [sendable data types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-data-types).

#### Modules to Import

import { collections } from '@kit.ArkTS';

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| length | number | Yes | No | Number of elements in a ConcatArray. |

#### \[index: number\]

readonly \[index: number\]: T

Returns the element at a given index in this ConcatArray.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the element. The index starts from zero. The element at the specified index cannot be modified. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Element in the ConcatArray. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Illegal index. |
| 10200001 | The value of index is out of range. |

**Example**

let concatArray : collections.ConcatArray<number> = new collections.Array<number>(1, 2, 4);
console.info("Element at index 1: ", concatArray\[1\]);

#### join

join(separator?: string): string

Concatenates all elements in this array into a string, with a given separator.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| separator | string | No | Separator to be used. If no value is passed in, a comma (,) is used as the separator. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String obtained. If the array is empty, an empty string is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Invalid separator. |

**Example**

let concatArray : collections.ConcatArray<string> = new collections.Array<string>('a', 'b', 'c');
let joinedString = concatArray.join('-'); // "a-b-c" is returned.

#### slice

slice(start?: number, end?: number): ConcatArray<T>

Selects a range of elements in this array to create an array.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| start | number | No | Start index of the range. If a negative number is passed in, it refers to the index of start + array.length. The default value is **0**. |
| end | number | No | End index of the range (exclusive). If a negative number is passed in, it refers to the index of end + array.length. The default value is the length of the ArkTS array. |

**Return value**

| Type | Description |
| :-- | :-- |
| ConcatArray<T> | New array containing the selected elements. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Invalid \`start\` or \`end\` parameters. |

**Example**

let concatArray : collections.ConcatArray<number> = new collections.Array<number>(1, 2, 3, 4, 5);
let slicedArray = concatArray.slice (1, 3); // \[2, 3\] is returned. The original array remains unchanged.
