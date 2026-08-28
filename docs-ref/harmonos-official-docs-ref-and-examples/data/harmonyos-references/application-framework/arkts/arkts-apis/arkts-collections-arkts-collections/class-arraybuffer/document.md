# Class (ArrayBuffer)

Underlying data structure of the ArkTS TypedArray ([Int8Array](../class-int8array/document.md), [Uint8Array](../class-uint8array/document.md), [Int16Array](../class-int16array/document.md), [Uint16Array](../class-uint16array/document.md), [Int32Array](../class-int32array/document.md), [Uint32Array](../class-uint32array/document.md), [Uint8ClampedArray](../class-uint8clampedarray/document.md), and [Float32Array](../class-float32array/document.md)).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/MFlRN8oSQO6lo7oK0062dw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062222Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FB5300CD5D11B38908F031E4B36B0F84C79F0A59826A3FBF0269464964FA4F6)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module can be imported only to ArkTS files (with the file name extension .ets).
    

**Decorator**: @Sendable

#### Modules to Import

import { collections } from '@kit.ArkTS';

#### Properties

**System capability**: SystemCapability.Utils.Lang

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| byteLength | number | Yes | No | Number of bytes occupied by the buffer. |

#### constructor

constructor(byteLength: number)

A constructor used to create an ArkTS ArrayBuffer of a given length.

**System capability**: SystemCapability.Utils.Lang

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| byteLength | number | Yes | Number of bytes occupied by the buffer. The maximum value is **2147483647**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 10200012 | The ArrayBuffer's constructor cannot be directly invoked. |

**Example**

let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(10);
console.info("byteLength: " + arrayBuffer.byteLength); // byteLength: 10

#### slice

slice(begin: number, end?: number): ArrayBuffer

Selects a range of elements in this ArkTS ArrayBuffer to create an ArkTS ArrayBuffer.

**System capability**: SystemCapability.Utils.Lang

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| begin | number | Yes | Start index of the range. If a negative number is passed in, it refers to the index of begin + arrayBuffer.byteLength. |
| end | number | No | End index of the range (exclusive). If a negative number is passed in, it refers to the index of end + arrayBuffer.byteLength. The default value is the length of the original ArkTS ArrayBuffer. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | New ArrayBuffer generated. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 10200011 | The slice method cannot be bound. |
| 10200201 | Concurrent modification error. |

**Example**

let arrayBuffer: collections.ArrayBuffer = new collections.ArrayBuffer(10);
let slicedBuffer: collections.ArrayBuffer = arrayBuffer.slice(0, 4);
console.info("byteLength: " + slicedBuffer.byteLength); // byteLength: 4
