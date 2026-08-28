# @ohos.convertxml (XML-to-JavaScript Conversion)

The convertxml module provides APIs for converting XML text into JavaScript objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/kkXVgAv9RTO4d38hxi5dsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91B43DFFBD44FD8779BB8A867A3FCFC63767C403F9ED6EE2157FC1D9D9DD52F0)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { convertxml } from '@kit.ArkTS';

#### ConvertXML

#### \[h2\]fastConvertToJSObject14+

fastConvertToJSObject(xml: string, options?: ConvertOptions) : Object

Converts an XML text to an object of the object type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/hQi_ihAUSpOSLGrwEFHwSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13DDBA8BE245702104764C57AE7E0147573EA3C43FFAA7BAF186F18E6E3B5C7F)

-   This API cannot parse XML files with a large amount of data. If the text content of a single element exceeds 10 MB, an error message is displayed and an object that contains only the XML tag header will be returned.
    
-   In Windows, a newline is usually represented by the carriage return (CR) followed by the line feed (LF). However, the object obtained by calling this API uses only the LF to indicate a new line.
    

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| xml | string | Yes | XML text to convert. If the XML text contains the ampersand (&), replace it with the entity reference **&amp;**. |
| options | [ConvertOptions](#convertoptions) | No | Options for conversion. The default value is a **ConvertOptions** object, which consists of the default values of the attributes in the object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | JavaScript object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200002 | Invalid xml string. |

**Example**

try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '   <title>Hello\\r\\nWorld</title>' +
    '   <todo><!\[CDATA\[Work\\r\\n\]\]></todo>' +
    '</note>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "\_declaration",
    instructionKey: "\_instruction",
    attributesKey: "\_attributes",
    textKey: "\_text",
    cdataKey: "\_cdata",
    doctypeKey: "\_doctype",
    commentKey: "\_comment",
    parentKey: "\_parent",
    typeKey: "\_type",
    nameKey: "\_name",
    elementsKey: "\_elements"
  };
  let result = JSON.stringify(conv.fastConvertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// Output (non-compact)
// {"\_declaration":{"\_attributes":{"version":"1.0","encoding":"utf-8"}},"\_elements":\[{"\_type":"element","\_name":"note","\_attributes":{"importance":"high","logged":"true"},"\_elements":\[{"\_type":"element","\_name":"title","\_elements":\[{"\_type":"text","\_text":"Hello\\nWorld"}\]},{"\_type":"element","\_name":"todo","\_elements":\[{"\_type":"cdata","\_cdata":"Work\\n"}\]}\]}\]}

#### \[h2\]convertToJSObject(deprecated)

convertToJSObject(xml: string, options?: ConvertOptions) : Object

Converts an XML text to an object of the object type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/5UB1v51qRHea31NzK9tZ3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D90DB20DE106A51BC7D92E9CC50A32E3EC5E5891D54C2339F776EC5EB55C4E17)

This API is supported since API version 9 and deprecated since API version 14. You are advised to use [fastConvertToJSObject14+](#fastconverttojsobject14) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| xml | string | Yes | XML text to convert. If the XML text contains the ampersand (&), replace it with the entity reference **&amp;**. |
| options | [ConvertOptions](#convertoptions) | No | Options for conversion. The default value is a **ConvertOptions** object, which consists of the default values of the attributes in the object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | JavaScript object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200002 | Invalid xml string. |

**Example**

try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
      '<note importance="high" logged="true">' +
      '    <title>Happy</title>' +
      '    <todo>Work</todo>' +
      '    <todo>Play</todo>' +
      '</note>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "\_declaration",
    instructionKey: "\_instruction",
    attributesKey: "\_attributes",
    textKey: "\_text",
    cdataKey: "\_cdata",
    doctypeKey: "\_doctype",
    commentKey: "\_comment",
    parentKey: "\_parent",
    typeKey: "\_type",
    nameKey: "\_name",
    elementsKey: "\_elements"
  };
  let result = JSON.stringify(conv.convertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// Output (non-compact)
// {"\_declaration":{"\_attributes":{"version":"1.0","encoding":"utf-8"}},"\_elements":\[{"\_type":"element","\_name":"note","\_attributes":{"importance":"high","logged":"true"},"\_elements":\[{"\_type":"element","\_name":"title","\_elements":\[{"\_type":"text","\_text":"Happy"}\]},{"\_type":"element","\_name":"todo","\_elements":\[{"\_type":"text","\_text":"Work"}\]},{"\_type":"element","\_name":"todo","\_elements":\[{"\_type":"text","\_text":"Play"}\]}\]}\]}

#### \[h2\]convert(deprecated)

convert(xml: string, options?: ConvertOptions) : Object

Converts an XML text into a JavaScript object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/72AoAAPbQBmML-OZP5cSnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC4126E93E6ABCCCE28D20F4AB12129DB39C734AF634F8F23AA44BAD38FB3E87)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [fastConvertToJSObject14+](#fastconverttojsobject14) instead.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| xml | string | Yes | XML text to convert. |
| options | [ConvertOptions](#convertoptions) | No | Options for conversion. The default value is a **ConvertOptions** object, which consists of the default values of the attributes in the object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Object | JavaScript object. |

**Example**

let xml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title>Happy</title>' +
    '    <todo>Work</todo>' +
    '    <todo>Play</todo>' +
    '</note>';
let conv = new convertxml.ConvertXML();
let options: convertxml.ConvertOptions = {
  trim: false,
  declarationKey: "\_declaration",
  instructionKey: "\_instruction",
  attributesKey: "\_attributes",
  textKey: "\_text",
  cdataKey: "\_cdata",
  doctypeKey: "\_doctype",
  commentKey: "\_comment",
  parentKey: "\_parent",
  typeKey: "\_type",
  nameKey: "\_name",
  elementsKey: "\_elements"
};
let result = JSON.stringify(conv.convert(xml, options));
console.info(result);
// Output (non-compact)
// {"\_declaration":{"\_attributes":{"version":"1.0","encoding":"utf-8"}},"\_elements":\[{"\_type":"element","\_name":"note","\_attributes":{"importance":"high","logged":"true"},"\_elements":\[{"\_type":"element","\_name":"title","\_elements":\[{"\_type":"text","\_text":"Happy"}\]},{"\_type":"element","\_name":"todo","\_elements":\[{"\_type":"text","\_text":"Work"}\]},{"\_type":"element","\_name":"todo","\_elements":\[{"\_type":"text","\_text":"Play"}\]}\]}\]}

#### ConvertOptions

Options for conversion.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| trim | boolean | No | No | Whether to trim the whitespace characters before and after the text. The value **true** means to trim the whitespace characters before and after the text, and **false** means to keep them. |
| ignoreDeclaration | boolean | No | Yes | Whether to ignore the XML declaration. The value **true** means to ignore the XML declaration, and **false** means the opposite. The default value is **false**. |
| ignoreInstruction | boolean | No | Yes | Whether to ignore the XML processing instruction. The value **true** means to ignore the XML processing instruction, and **false** means the opposite. The default value is **false**. |
| ignoreAttributes | boolean | No | Yes | Whether to ignore the element's attribute information. The value **true** means to ignore the element's attribute information, and **false** means the opposite. The default value is **false**. |
| ignoreComment | boolean | No | Yes | Whether to ignore element comments. The value **true** means to ignore element comments, and **false** means the opposite. The default value is **false**. |
| ignoreCDATA | boolean | No | Yes | Whether to ignore the element's CDATA information. The value **true** means to ignore the element's CDATA information, and **false** means the opposite. The default value is **false**. |
| ignoreDoctype | boolean | No | Yes | Whether to ignore the element's Doctype information. The value **true** means to ignore the element's Doctype information, and **false** means the opposite. The default value is **false**. |
| ignoreText | boolean | No | Yes | Whether to ignore the element's text information. The value **true** means to ignore the element's text information, and **false** means the opposite. The default value is **false**. |
| declarationKey | string | No | No | Name of the attribute key for **declaration** in the output object. |
| instructionKey | string | No | No | Name of the attribute key for **instruction** in the output object. |
| attributesKey | string | No | No | Name of the attribute key for **attributes** in the output object. |
| textKey | string | No | No | Name of the attribute key for **text** in the output object. |
| cdataKey | string | No | No | Name of the attribute key for **cdata** in the output object. |
| doctypeKey | string | No | No | Name of the attribute key for **doctype** in the output object. |
| commentKey | string | No | No | Name of the attribute key for **comment** in the output object. |
| parentKey | string | No | No | Name of the attribute key for **parent** in the output object. |
| typeKey | string | No | No | Name of the attribute key for **type** in the output object. |
| nameKey | string | No | No | Name of the attribute key for **name** in the output object. |
| elementsKey | string | No | No | Name of the attribute key for **elements** in the output object. |
