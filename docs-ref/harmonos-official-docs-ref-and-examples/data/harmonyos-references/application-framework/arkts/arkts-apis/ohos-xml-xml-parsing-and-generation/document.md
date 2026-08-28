# @ohos.xml (XML Parsing and Generation)

The xml module provides APIs for generating and parsing XML files.

The module offers two methods for generating XML files:

-   [XmlSerializer](#xmlserializer): suitable for scenarios where the size of the XML text is known in advance.
-   [XmlDynamicSerializer20+](#xmldynamicserializer20): suitable for scenarios where the size of the XML text is not known in advance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/2-qzjigeTKimsUHZEDw22w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3B4910A583C31B14B079542D40064F3596A12E75B423D7862671D4830A3D3B5)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { xml } from '@kit.ArkTS';

#### XmlSerializer

**XmlSerializer** provides APIs to generate an XML file.

#### \[h2\]constructor

constructor(buffer: ArrayBuffer | DataView, encoding?: string)

A constructor used to create an **XmlSerializer** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/kxPF61X6QcqHb6ZMxv93Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AB47EEC74FEB5EB0D67659E533C3FAE631D5171793FA9E2480BCB33F5FDF3C3)

The buffer is used to temporarily store XML text generated. Its size can be customized. Ensure that the buffer is large enough to hold the generated text.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | DataView | Yes | ArrayBuffer or DataView for storing the XML information to set. |
| encoding | string | No | Encoding format. The default value is **'utf-8'** (the only format currently supported). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer, "utf-8");

#### \[h2\]setAttributes

setAttributes(name: string, value: string): void

Sets an attribute.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ISUnROrEQ_6Jh1qzOupbtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED101B2C3B207C2CCEAB185396D5AA1C6C12F390BA2EC441E7DE36D5AF305C12)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add an attribute name starting with a digit or add multiple attributes with the same name.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the attribute. |
| value | string | Yes | Value of the attribute. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setAttributes("importance", "high");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high"/>

#### \[h2\]addEmptyElement

addEmptyElement(name: string): void

Adds an empty element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3YAlEThHQH6Z4xa9Vm0iuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E34F362B1DE315DA93EF0C0FAC191BD781BD23DFDC7C98404E55BAEFD0785363)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add an attribute name starting with a digit.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.addEmptyElement("d");
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <d/>

#### \[h2\]setDeclaration

setDeclaration(): void

Sets a file declaration with encoding.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setDeclaration();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <?xml version="1.0" encoding="utf-8"?>

#### \[h2\]startElement

startElement(name: string): void

Adds the start tag based on the given element name.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Uy-CEsLlSIuAgqALuLjJXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02F80BA2D700C8E05188BBA016D4DF1D01903D9DC7F330A01731A2181C38F826)

-   After calling this API, you must call [endElement](#endelement) to write the end flag to ensure that the node is closed correctly.
    
-   This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add an attribute name starting with a digit.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <note>Happy</note>

#### \[h2\]endElement

endElement(): void

Adds the end tag of the element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ZdholfvAS2yNyMOcRMTAGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9E06936AA24B705457DEEB75E696D3DE5D1845F1F7EE354445E5C45D7081587)

Before calling this API, you must call [startElement](#startelement) to write the start flag.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <note>Happy</note>

#### \[h2\]setNamespace

setNamespace(prefix: string, namespace: string): void

Sets the namespace for an element tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ajOAcPZ2Sq-ELzY55G-8oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58D5A775A54BB67987A7C458E0874D30E03460796ADE673E941636A6C209E05C)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add a namespace starting with a digit or set multiple namespaces for the same element.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | Prefix of the element and its child elements. |
| namespace | string | Yes | Namespace to set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setNamespace("h", "http://www.w3.org/TR/html4/");
thatSer.startElement("note");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <h:note xmlns:h="http://www.w3.org/TR/html4/"/>

#### \[h2\]setComment

setComment(text: string): void

Sets a comment.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Comment to set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setComment("Hello, World!");
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!--Hello, World!-->

#### \[h2\]setCDATA

setCDATA(text: string): void

Adds data to the CDATA tag. The structure of the generated CDATA tag is "<! <!\[CDATA\["+ Data added + "\]\]>".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/dn15zDHDSAOiL5H_Bv-tWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9000A9B84AF86734FBD1EB0916E9C8B4EF16335906CA0E468127ED54CA25DFBB)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add data that contains the string \]\]> to the CDATA tag.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | CDATA data to set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setCDATA('root SYSTEM')
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!\[CDATA\[root SYSTEM\]\]>

#### \[h2\]setText

setText(text: string): void

Sets a tag value.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Tag value to set, which is the content of the **text** attribute. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setAttributes("importance", "high");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high">Happy</note>

#### \[h2\]setDocType

setDocType(text: string): void

Sets a document type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Content of **DocType** to set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">

#### XmlDynamicSerializer20+

The **XmlDynamicSerializer** class is used to dynamically generate XML strings. It is recommended when the length of the XML content cannot be determined in advance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/QbbgeUiaQCOSwxGHf76AXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A660556F5EAC7237AB4A032B69072740186A74199E401A5B50D17561CB824491)

Objects constructed from this class do not require manual creation of an ArrayBuffer. You can continuously add XML elements, and the upper limit for the length of the final serialized string result is 100,000 characters.

#### \[h2\]constructor20+

constructor(encoding?: string)

A constructor used to create an **XmlDynamicSerializer** instance.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| encoding | string | No | Encoding format. The default value is **'utf-8'** (the only format currently supported). |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200066 | Incorrect encoding format, only support utf-8. |

**Example**

let serializer = new xml.XmlDynamicSerializer('utf-8');

#### \[h2\]getOutput20+

getOutput(): ArrayBuffer

Obtains the ArrayBuffer of the XML string.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | ArrayBuffer for storing the XML information to set. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arr = serializer.getOutput();
let uint8 = new Uint8Array(arr);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>

#### \[h2\]setAttributes20+

setAttributes(name: string, value: string): void

Sets an attribute.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/aYoP3sy9QdGhuS-Pa_FXQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B42EEB2D9943A1954015D19E7F21AD13F6F94D6284EA367A5FD1D000F6B0CFA3)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add an attribute name starting with a digit or add multiple attributes with the same name.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Key of the attribute. The total length of the XML cannot exceed 100,000 characters. This field cannot be empty. |
| value | string | Yes | Value of the attribute. The total length of the XML cannot exceed 100,000 characters. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200063 | Illegal position for xml. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setAttributes("importance", "high");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high"/>

#### \[h2\]addEmptyElement20+

addEmptyElement(name: string): void

Adds an empty element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/OkSY5hP0Tfu7bwfIelY9Pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E616D5FAA9AA66389570A0B18CE724523B8C6D23871A5B2361BA9ECD6C1DE51)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add an attribute name starting with a digit.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the empty element. The total length of the XML cannot exceed 100,000 characters. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.addEmptyElement("d");
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <d/>

#### \[h2\]setDeclaration20+

setDeclaration(): void

Sets a file declaration with encoding.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200063 | Illegal position for xml. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setDeclaration();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <?xml version="1.0" encoding="utf-8"?>

#### \[h2\]startElement20+

startElement(name: string): void

Writes the start tag of the element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/onT0Y5uNQ5a4m7AidRaBzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20F8B60E18C32006F9201E51280B0EBDEDC05E519BA88FD5C039649EC2F51B55)

-   After calling this API, you must call [endElement](#endelement) to write the end flag to ensure that the node is closed correctly.
    
-   This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add an attribute name starting with a digit.
    

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the element. The total length of the XML cannot exceed 100,000 characters. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>

#### \[h2\]endElement20+

endElement(): void

Writes the end tag of the element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Pcjq2H4jSUuw3EdeRXvMSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FE16CE76E51D0F1E96CFC9A83B1576DCF2D8BF4DA8ADB0D15DB0743AA45844B)

Before calling this API, you must call [startElement](#startelement) to write the start flag.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200065 | There is no match between the startElement and the endElement. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>

#### \[h2\]setNamespace20+

setNamespace(prefix: string, namespace: string): void

Sets the namespace for an element tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/GkFcfgv7TSe5Zc2G3HtTPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1EE552FA1A5CEA202B00E73CABF96384B121F4E8F8A7713BEC1C5BE00B018A0)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add a namespace starting with a digit or set multiple namespaces for the same element.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | Prefix of the element and its child elements. The total length of the XML cannot exceed 100,000 characters. This field cannot be empty. |
| namespace | string | Yes | Namespace to set. The total length of the XML cannot exceed 100,000 characters. This field cannot be empty. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setNamespace("h", "http://www.w3.org/TR/html4/");
serializer.startElement("note");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <h:note xmlns:h="http://www.w3.org/TR/html4/"/>

#### \[h2\]setComment20+

setComment(text: string): void

Sets a comment.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Comment to set. The total length of the XML cannot exceed 100,000 characters. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setComment("Hello, World!");
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!--Hello, World!-->

#### \[h2\]setCdata20+

setCdata(text: string): void

Adds data to the CDATA tag. The structure of the generated CDATA tag is "<! <!\[CDATA\["+ Data added + "\]\]>".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/LCF8uqw3QUGh4XtAjs3Ctg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DEAA41BEB31688692080895AB3E83A995B315EA8AB9BFAA6774F72AFF85E1BD)

This API does not perform standard XML verification on the data to add. Ensure that the data complies with the XML specifications. For example, as stipulated in the specifications, you are not allowed to add data that contains the string \]\]> to the CDATA tag.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | CDATA data to set. The total length of the XML cannot exceed 100,000 characters. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setCdata('root SYSTEM')
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!\[CDATA\[root SYSTEM\]\]>

#### \[h2\]setText20+

setText(text: string): void

Sets a tag value.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Tag value. The total length of the XML cannot exceed 100,000 characters. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setAttributes("importance", "high");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high">Happy</note>

#### \[h2\]setDocType20+

setDocType(text: string): void

Sets a document type.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Content of **DocType** to set. The total length of the XML cannot exceed 100,000 characters. |

**Error codes**

For details about the error codes, see [Utils Error Codes](../../error-codes/utils-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10200062 | The cumulative length of xml has exceeded the upper limit 100000. |
| 10200064 | Cannot be an empty string. |

**Example**

import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">

#### XmlPullParser

Implements XML file parsing.

#### \[h2\]constructor

constructor(buffer: ArrayBuffer | DataView, encoding?: string)

Creates and returns an **XmlPullParser** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | DataView | Yes | XML text information to be parsed. |
| encoding | string | No | Encoding format. The default value is **'utf-8'** (the only format currently supported). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { util } from '@kit.ArkTS';

let strXml = '<title>Happy</title>'
let textEncoder = new util.TextEncoder();
let uint8Array = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(uint8Array.buffer as object as ArrayBuffer, 'UTF-8');

#### \[h2\]parseXml14+

parseXml(option: ParseOptions): void

Parses XML information.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [ParseOptions](#parseoptions) | Yes | XML parsing options. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

For details, see [Parsing XML Tags and Values](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/xml-parsing#parsing-xml-tags-and-values) and [Parsing XML Attributes and Values](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/xml-parsing#parsing-xml-attributes-and-values).

import { xml, util } from '@kit.ArkTS';

let strxml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title><!\[CDATA\[Test\\nTest\]\]></title>' +
    '</note>';
let textEncoder = new util.TextEncoder();
let uint8 = textEncoder.encodeInto(strxml);

function func(key: xml.EventType, value: xml.ParseInfo) {
  if (key == xml.EventType.CDSECT) {
    console.info(JSON.stringify(value.getText()));
  }
  return true;
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
let pullParser = new xml.XmlPullParser(uint8.buffer as object as ArrayBuffer);
pullParser.parseXml(options);
// "Test\\nTest"

#### \[h2\]parse(deprecated)

parse(option: ParseOptions): void

Parses XML information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/HFiZKok0RAuex9ai3Ivqbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7661A74DDEE66909FCC75AD789922C6CE526C1733444192BF9219F0C603CC625)

This API is supported since API version 8 and deprecated since API version 14. You are advised to use [parseXml14+](#parsexml14) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [ParseOptions](#parseoptions) | Yes | XML parsing options. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
    '<company>John &amp; Hans</company>' +
    '<title>Happy</title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
let str = '';
function func(name: string, value: string) {
  str = name + value;
  console.info(str);
  return true;
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tagValueCallbackFunction:func}
that.parse(options);
// note
// company
// John & Hans
// company
// title
// Happy
// title
// note

#### AttributeWithTagCb20+

type AttributeWithTagCb = (tagName: string, key: string, value: string) => boolean

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tagName | string | Yes | Tag name. |
| key | string | Yes | Attribute name. |
| value | string | Yes | Attribute value. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | A Boolean value that indicates whether to continue parsing the tag name, attribute name, and attribute value. The value **true** indicates that the parsing continues, and the value **false** indicates that the parsing stops. |

#### ParseOptions

Defines the XML parsing options.

**System capability**: SystemCapability.Utils.Lang

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| supportDoctype | boolean | No | Yes | 
Whether to parse the document type. The value **true** means to parse the document type, and **false** means the opposite. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ignoreNameSpace | boolean | No | Yes | 

Whether to ignore the namespace. If the namespace is ignored, it will not be parsed. The value **true** means to ignore the namespace, and **false** means the opposite. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| tagValueCallbackFunction | (name: string, value: string) => boolean | No | Yes | 

Start tag, tag value, and end tag of parsing. The default value is **undefined**, indicating no parsing.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| attributeValueCallbackFunction | (name: string, value: string) => boolean | No | Yes | 

Parsing attribute and attribute value. The default value is **undefined**, indicating no parsing.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| tokenValueCallbackFunction | (eventType: [EventType](#eventtype), value: [ParseInfo](#parseinfo)) => boolean | No | Yes | 

Parsing element's [EventType](#eventtype) and [ParseInfo](#parseinfo). The default value is **undefined**, indicating no parsing.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| attributeWithTagCallbackFunction20+ | [AttributeWithTagCb](#attributewithtagcb20) | No | Yes | 

Tag name, attribute name, and attribute value of parsing. The default value is **undefined**, indicating that no parsing is performed.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ParseInfo

Provides APIs to manage the parsed XML information.

#### \[h2\]getColumnNumber

getColumnNumber(): number

Obtains the current column number, starting from 1.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Column number obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getColumnNumber() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:1 key:2 value:45 key:4 value:50 key:3 value:57 key:1 value:57

#### \[h2\]getDepth

getDepth(): number

Obtains the depth of this element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/qerSyc74TrqqYH_1Ex1Pwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062225Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEC012A0D9A1CB3ACBD6D320B87B642AA6E4723A549B9B90110DDB13D1A89710)

The depth of the whitespace character event in the tag is the same as the depth of the tag.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Depth obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high">' +
    '<title>Happy</title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getDepth() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:0 key:2 value:1 key:2 value:2 key:4 value:2 key:3 value:2 key:3 value:1 key:1 value:0

#### \[h2\]getLineNumber

getLineNumber(): number

Obtains the current line number, starting from 1.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Line number obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Work</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getLineNumber() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:1 key:2 value:1 key:4 value:1 key:3 value:1 key:1 value:1

#### \[h2\]getName

getName(): string

Obtains the name of this element.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | Element name obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getName() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value:note key:4 value: key:3 value:note key:1 value:

#### \[h2\]getNamespace

getNamespace(): string

Obtains the namespace of this element.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | Namespace obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note xmlns:h="http://www.w3.org">' +
    '<h:title>Happy</h:title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getNamespace() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:false, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value: key:2 value:http://www.w3.org key:4 value: key:3 value:http://www.w3.org key:3 value: key:1 value:

#### \[h2\]getPrefix

getPrefix(): string

Obtains the prefix of this element.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | Element prefix obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note xmlns:h="http://www.w3.org/TR/html4">' +
    '<h:title>Happy</h:title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getPrefix() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:false, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value: key:2 value:h key:4 value: key:3 value:h key:3 value: key:1 value:

#### \[h2\]getText

getText(): string

Obtains the text of the current event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| string | Text content obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note>Happy</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getText() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value: key:2 value: key:4 value:Happy key:3 value: key:1 value:

#### \[h2\]isEmptyElementTag

isEmptyElementTag(): boolean

Checks whether the current element is empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | If **true** is returned, the current element is empty. If **false** is returned, the current element is not empty. |

**Example**

import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
    '<title/>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.isEmptyElementTag() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:false key:2 value:false key:2 value:true key:3 value:false key:3 value:false key:1 value:false

#### \[h2\]isWhitespace

isWhitespace(): boolean

Checks whether the current event contains only whitespace characters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the text event contains only whitespace characters; otherwise, **false** is returned. |

**Example**

import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
    '<title> </title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.isWhitespace() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:true key:2 value:false key:2 value:true key:10 value:true key:3 value:true key:3 value:true key:1 value:true

#### \[h2\]getAttributeCount

getAttributeCount(): number

Obtains the number of attributes for the current start tag.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of attributes obtained. |

**Example**

import { util } from '@kit.ArkTS';

let strXml = '<?xml version="1.0" encoding="utf-8"?><note importance="high" logged="true"/>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer);
let str = "";
function func(key: xml.EventType, value: xml.ParseInfo) {
  str += 'key:' + key + ' value:' + value.getAttributeCount() + ' ';
  return true; // Determines whether to continually parse, which is used to continue or terminate parsing.
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
that.parseXml(options);
console.info(str);
// key:0 value:0 key:2 value:2 key:3 value:2 key:1 value:0

#### EventType

Enumerates the event types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Utils.Lang

| Name | Value | Description |
| :-- | :-- | :-- |
| START\_DOCUMENT | 0 | Start document event. |
| END\_DOCUMENT | 1 | End document event. |
| START\_TAG | 2 | Start tag event. |
| END\_TAG | 3 | End tag event. |
| TEXT | 4 | Text event. |
| CDSECT | 5 | CDATA section event. |
| COMMENT | 6 | XML comment event. |
| DOCDECL | 7 | XML document type declaration event. |
| INSTRUCTION | 8 | XML processing instruction event. |
| ENTITY\_REFERENCE | 9 | Entity reference event. |
| WHITESPACE | 10 | Whitespace character event. |
