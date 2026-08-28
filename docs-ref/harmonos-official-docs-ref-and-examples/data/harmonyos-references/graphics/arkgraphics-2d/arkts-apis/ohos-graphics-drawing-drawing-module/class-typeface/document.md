# Class (Typeface)

Describes the style of a typeface, such as SimSun or KaiTi.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/JgiXK2aqR02lfSJKV0SUaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A89CB98BE1C7C87388F42AE763F3BBBB71BFFD0F5FC46FA95149F713B8FC7F0)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module uses the physical pixel unit, px.
    
-   The module operates under a single-threaded model. The caller needs to manage thread safety and context state transitions.
    

#### Modules to Import

import { drawing } from '@kit.ArkGraphics2D';

#### getFamilyName

getFamilyName(): string

Obtains the name of the typeface family, which is the name given to a collection of related typeface designs.

**System capability**: SystemCapability.Graphics.Drawing

**Returns**

| Type | Description |
| :-- | :-- |
| string | Family name. |

**Example**

import { drawing } from '@kit.ArkGraphics2D';

const font = new drawing.Font();
let typeface = font.getTypeface();
let familyName = typeface.getFamilyName();

#### makeFromCurrent20+

makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface

Constructs a typeface object from the current typeface and its arguments.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| typefaceArguments | [TypefaceArguments](../class-typefacearguments/document.md) | Yes | Typeface arguments. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Typeface](#) | Typeface object. In abnormal cases, a null pointer is returned. |

**Example**

import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let typeArguments = new drawing.TypefaceArguments();
    typeArguments.addVariation("wght", 100);
    const myTypeFace = drawing.Typeface.makeFromFile("/system/fonts/HarmonyOS\_Sans\_SC.ttf");
    const typeFace1 = myTypeFace.makeFromCurrent(typeArguments);
    let font = new drawing.Font();
    font.setTypeface(typeFace1);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}

#### makeFromFile12+

static makeFromFile(filePath: string): Typeface

Constructs a typeface from a file.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Path of the file. For details, see [Mappings Between Application Sandbox Paths and Physical Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#mappings-between-application-sandbox-paths-and-physical-paths). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Typeface](#) | Typeface object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**Example**

import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    let str = "/system/fonts/HarmonyOS\_Sans\_Italic.ttf";
    const mytypeface = drawing.Typeface.makeFromFile(str);
    font.setTypeface(mytypeface);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}

#### makeFromRawFile18+

static makeFromRawFile(rawfile: Resource): Typeface

Constructs a typeface from a file, which must be stored in the **resources/rawfile** directory of the application project.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rawfile | [Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) | Yes | Resource object corresponding to the file. Currently, only resource objects referenced in **$rawfile** format are supported. The corresponding format is **$rawfile('filePath')**, where **filePath** is the relative path of the file to the **resources/rawfile** directory in the project. If the file is stored in **resources/rawfile**, the reference format is **$rawfile('HarmonyOS\_Sans\_Bold.ttf')**. If the file is stored in a subdirectory, for example, in **resources/rawfile/ttf**, the reference format is **$rawfile('ttf/HarmonyOS\_Sans\_Bold.ttf')**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Typeface](#) | Typeface object. In abnormal cases, a null pointer is returned. |

**Example**

import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    const myTypeFace = drawing.Typeface.makeFromRawFile($rawfile('HarmonyOS\_Sans\_Bold.ttf'));
    font.setTypeface(myTypeFace);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}

#### makeFromFileWithArguments20+

static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface

Constructs a typeface from the typeface file path and arguments.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Path of the file. For details, see [Mappings Between Application Sandbox Paths and Physical Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#mappings-between-application-sandbox-paths-and-physical-paths). |
| typefaceArguments | [TypefaceArguments](../class-typefacearguments/document.md) | Yes | Typeface arguments. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Typeface](#) | Typeface object. In abnormal cases, a null pointer is returned. |

**Example**

import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    let str = "/system/fonts/HarmonyOS\_Sans\_Italic.ttf";
    let typeFaceArgument = new drawing.TypefaceArguments();
    const myTypeFace = drawing.Typeface.makeFromFileWithArguments(str, typeFaceArgument);
    font.setTypeface(myTypeFace);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}

#### makeFromRawFileWithArguments20+

static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface

Constructs a typeface from a file with typeface arguments, which must be stored in the **resources/rawfile** directory of the application project.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rawfile | [Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource) | Yes | Resource object corresponding to the file. Currently, only resource objects referenced in **$rawfile** format are supported. The corresponding format is **$rawfile('filePath')**, where **filePath** is the relative path of the file to the **resources/rawfile** directory in the project. |
| typefaceArguments | [TypefaceArguments](../class-typefacearguments/document.md) | Yes | Typeface arguments. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Typeface](#) | Typeface object. In abnormal cases, a null pointer is returned. |

**Example**

import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class TextRenderNode extends RenderNode {
  async draw(context: DrawContext) {
    const canvas = context.canvas;
    let font = new drawing.Font();
    let typeFaceArgument = new drawing.TypefaceArguments();
    const myTypeFace = drawing.Typeface.makeFromRawFileWithArguments($rawfile('HarmonyOS\_Sans\_Bold.ttf'), typeFaceArgument);
    font.setTypeface(myTypeFace);
    const textBlob = drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT\_ENCODING\_UTF8);
    canvas.drawTextBlob(textBlob, 60, 100);
  }
}
