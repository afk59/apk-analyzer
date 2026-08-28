# DocumentScanner (Document Scanning Control)

The document scanning control provides the service of taking photos of documents and converting them into high-definition scanned copies. Users can capture document photos with their phones, and these photos can be automatically cropped, optimized, and then saved or shared as JPEG images or PDF files. Users can also use this service to identify tables from photos just taken or those in the gallery and generate table documents.

**Start version**: 5.0.0(12)

#### Module Import

import { DocType, DocumentScanner, DocumentScannerConfig, SaveOption, FilterId, ShootingMode, EditTab, DocumentScannerResultCallback } from "@kit.VisionKit";

#### DocumentScanner

Document scanning control, which can be integrated to implement document scanning.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Decorator type**: [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component)

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

scannerConfig

 | 

[DocumentScannerConfig](#section172439207710)

 | 

Yes

 | 

\-

 | 

Document scanning capability configuration.

 |
| 

onResult

 | 

[DocumentScannerResultCallback](#section3361123418402)

 | 

Yes

 | 

\-

 | 

Callback of the document scanning result.

 |

#### DocumentScannerConfig

Document scanning capability configuration.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxShotCount

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of document photos captured each time. The default value is **1**. The maximum value is **50**.

The value is an integer ranging from 1 to 50.

 |
| 

supportType

 | 

[DocType](#section11985750145117)\[\]

 | 

No

 | 

No

 | 

Supported file types. The default value is **\[DocType.DOC\]**.

**Device behavior differences**: Some device models support only **\[DocType.DOC\]**. If an unsupported value is set for a device model, the default value will be used.

 |
| 

isGallerySupported

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether images can be selected from the gallery.

-   **true**: yes
-   **false**: no

The default value is **true**.

 |
| 

defaultFilterId

 | 

[FilterId](#section4378024251)

 | 

No

 | 

Yes

 | 

Initial filter effect. By default, the enhanced filter is used.

 |
| 

editTabs

 | 

[EditTab](#section15162521671)\[\]

 | 

No

 | 

Yes

 | 

Buttons displayed in the tab bar. By default, all buttons are displayed.

 |
| 

defaultShootingMode

 | 

[ShootingMode](#section1551617521717)

 | 

No

 | 

Yes

 | 

Initial shooting mode. By default, manual shooting is used.

 |
| 

isShareable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the sharing function is supported.

-   **true**: yes
-   **false**: no

The default value is **true**.

 |
| 

saveOptions

 | 

[SaveOption](#section147301239151120)\[\]

 | 

No

 | 

Yes

 | 

File formats for saving scanning results. The default values are **\[SaveOption.JPG, SaveOption.EXCEL\]**.

 |
| 

originalUris

 | 

string\[\]

 | 

No

 | 

Yes

 | 

Initially provided [image URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#media-file-uri) list. If the value is not empty, it is directly used to jump to the editing screen. The value is left empty by default. The maximum length of the array is 50. Images that do not meet the following specifications (unit: px) will be removed:

1\. The minimum length of a single side is 224, and the maximum length is 8000.

2\. The product of the image width and height is less than or equal to 6000 x 8000.

3\. The ratio of the image height to its width and the ratio of the image width to its height are less than or equal to 3.

NOTE:

This parameter became functional in version 5.0.5(17) and was a reserved parameter in earlier versions.

 |

#### DocType

Enumeration of supported file types.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DOC

 | 

0

 | 

Document.

 |
| 

SHEET

 | 

1

 | 

Table.

 |

#### FilterId

Enumeration of filters added to images.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ORIGINAL

 | 

0

 | 

Original image filter.

 |
| 

MONOCHROME

 | 

1

 | 

Black and white filter.

 |
| 

STRENGTHEN

 | 

2

 | 

Enhanced filter.

 |

#### ShootingMode

Enumeration of photo shooting modes.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

AUTO

 | 

0

 | 

Automatic shooting mode.

 |
| 

MANUAL

 | 

1

 | 

Manual shooting mode.

 |

#### EditTab

Enumeration of buttons in the tab bar.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ROTATE\_TAB

 | 

0

 | 

Rotate button.

 |
| 

DELETE\_TAB

 | 

1

 | 

Delete button.

 |
| 

RESHOOT\_TAB

 | 

2

 | 

Reshoot button.

 |

#### SaveOption

Enumeration of file formats for saving scanning results.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

JPG

 | 

0

 | 

JPEG.

 |
| 

PDF

 | 

1

 | 

PDF.

 |
| 

EXCEL

 | 

2

 | 

Excel.

 |

#### DocumentScannerResultCallback

type DocumentScannerResultCallback = (code: number, saveType: SaveOption, uris: string\[\]) => void

Callback of the document scanning result.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.Component.DocScan

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

code

 | 

number

 | 

Yes

 | 

Result code.

**\-1**: No result is returned.

**200**: The recognition is successful.

**1008601001**: invalid URIs.

NOTE:

The result code 1008601001 is supported since 5.0.5 (17).

 |
| 

saveType

 | 

[SaveOption](#section147301239151120)

 | 

Yes

 | 

Format in which the result is saved.

 |
| 

uris

 | 

string\[\]

 | 

Yes

 | 

Document URI list.

 |
