# Class (PathIterator)

Implements a path operation iterator. You can read path operation instructions by traversing the iterator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/aXKito86SJKWnLRDTzkIPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062447Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F23285477FED0009224863CCCAB653418E5A16D51CFF7CC491BED66E92CAB4C6)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 18.
    
-   This module uses the physical pixel unit, px.
    
-   The module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### Modules to Import

import { drawing } from '@kit.ArkGraphics2D';

#### constructor18+

constructor(path: Path)

Creates an iterator and binds it with a path.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | [Path](../class-path/document.md) | Yes | **Path** object bound to the iterator. |

**Example**

import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);

#### next18+

next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb

Retrieves the next operation in this path and moves the iterator to that operation.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| points | Array<[common2D.Point](../../ohos-graphics-common2d-common-data-types-of-2d-graphics/document.md#point12)\> | Yes | Array of coordinate points. The array length must be at least the offset plus 4 to ensure that the array can hold all types of path data. After the operation is executed, this array is overwritten. The number of coordinate points to be filled depends on the operation type. Specifically, for **MOVE**, fill one coordinate; for **LINE**, fill two coordinates; for **QUAD**, fill three coordinates; for **CONIC**, fill three coordinates and one weight value (a total of 3.5 groups); for **CUBIC**, fill four coordinates; for **CLOSE** and **DONE**, do not fill any coordinate points. |
| offset | number | No | Offset from the start of the array where writing begins. The default value is **0**. The value range is \[0, size - 4\], where **size** is the length of the coordinate point array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [PathIteratorVerb](../enums/document.md#pathiteratorverb18) | Path operation type contained in the iterator. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(10, 20);
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let verbStr: Array<string> = \["MOVE", "LINE", "QUAD", "CONIC", "CUBIC", "CLOSE", "DONE"\];
let pointCount: Array<number> = \[1,2,3,4,4,0,0\];
let points: Array<common2D.Point> = \[{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}\];
let offset = 0;
let verb = iter.next(points, offset);
let outputMessage: string = "pathIteratorNext: ";
outputMessage += "verb =" + verbStr\[verb\] + "; has " + pointCount\[verb\] + " pairs: ";
for (let j = 0; j < pointCount\[verb\] + offset; j++) {
  outputMessage += "\[" + points\[j\].x + ", " + points\[j\].y + "\]";
}
console.info(outputMessage);

#### peek18+

peek(): PathIteratorVerb

Retrieves the next operation in this path, without moving the iterator.

**System capability**: SystemCapability.Graphics.Drawing

**Returns**

| Type | Description |
| :-- | :-- |
| [PathIteratorVerb](../enums/document.md#pathiteratorverb18) | Path operation type contained in the iterator. |

**Example**

import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.peek();

#### hasNext18+

hasNext(): boolean

Checks whether there is any next operation in the path operation iterator.

**System capability**: SystemCapability.Graphics.Drawing

**Returns**

| Type | Description |
| :-- | :-- |
| boolean | Whether there is any next operation in the path operation iterator. **true** means yes; **false** otherwise. |

**Example**

import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.hasNext();
