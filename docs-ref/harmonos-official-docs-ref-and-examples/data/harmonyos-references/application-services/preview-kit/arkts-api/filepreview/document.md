# filePreview

This module provides convenient quick file preview capabilities for apps. Apps can use the system-level preview API provided by Preview Kit to quickly display the preview page, so that users can preview various files, such as images, videos, audios, texts, and HTML pages.

This module provides the capability of quick file preview, allowing your app to quickly open the preview window based on the file preview information.

The following file types support preview:

| 
Type

 | 

File Name Extension

 | 

mimeType

 |
| :-- | :-- | :-- |
| 

Text

 | 

txt, cpp, c, h, java, xhtml, xml

 | 

text/plain, text/x-c++src, text/x-csrc, text/x-chdr, text/x-java, application/xhtml+xml, text/xml

 |
| 

Web page

 | 

html, htm

 | 

text/html

 |
| 

Image

 | 

jpg, png, gif, webp, bmp, svg

 | 

image/jpeg, image/png, image/gif, image/webp, image/bmp, image/svg+xml

 |
| 

Audio

 | 

m4a, aac, mp3, ogg, wav

 | 

audio/mp4a-latm, audio/aac, audio/mpeg, audio/ogg, audio/x-wav

 |
| 

Video

 | 

mp4, mkv, ts

 | 

video/mp4, video/x-matroska, video/mp2ts

 |
| 

Folder

 | 

N/A

 | 

N/A

 |
| 

Document

 | 

pdf

 | 

application/pdf

**Start version**: 5.0.0(12)

 |
| 

Office document

 | 

doc, docx, xls, xlsx, ppt, pptx, csv, ofd

 | 

application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, text/csv, general.ofd

**Start version**: 5.0.0(12)

 |

**Start version**: 4.1.0(11)

#### Module Import

import { filePreview } from '@kit.PreviewKit';

#### PreviewInfo

File preview information, including the file title, URI, and file type (**mimeType**).

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

| 
Parameter

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

title

 | 

string

 | 

No

 | 

Yes

 | 

File title.

 |
| 

uri

 | 

string

 | 

No

 | 

No

 | 

File [URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro).

 |
| 

mimeType

 | 

string

 | 

No

 | 

No

 | 

Media resource type of the file, for example, **text/plain**.

NOTE:

If the media resource type cannot be determined, this field can be set to an empty string (''). The system will infer the type based on the URI suffix.

 |

#### DisplayInfo

Attribute values of the floating window, including its size and position.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

| 
Parameter

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

No

 | 

Start X-coordinate of the preview window, in pixels.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Start Y-coordinate of the preview window, in pixels.

 |
| 

width

 | 

number

 | 

No

 | 

Yes

 | 

Width of the preview window, in pixels.

 |
| 

height

 | 

number

 | 

No

 | 

Yes

 | 

Height of the preview window, in pixels.

 |

#### openPreview

openPreview(context: Context, file: PreviewInfo, info?: DisplayInfo): Promise<void>

Displays the preview window based on the file preview information and floating window attributes. Calling this API repeatedly within 1 second will not take effect. This API returns the result asynchronously through a promise.

The calling app must ensure that the provided URI supports delegated access.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

file

 | 

[PreviewInfo](#section1081123302517)

 | 

Yes

 | 

File preview information. The **title** parameter is optional. If **title** is left blank, **URI** will be parsed. If **URI** cannot be parsed, the file will be marked as an unknown file.

 |
| 

info

 | 

[DisplayInfo](#section177311614561)

 | 

No

 | 

Modal window display information. If this parameter is not set for 2-in-1 devices, a window of the default size will be displayed. This parameter is invalid for mobile phones and tablets.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let displayInfo: filePreview.DisplayInfo = {
  x: 100,
  y: 100,
  width: 800,
  height: 800
};
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.openPreview(uiContext, fileInfo, displayInfo).then(() => {
  console.info('Succeeded in opening preview');
}).catch((err: BusinessError) => {
  console.error(\`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}\`);
});

#### openPreview

openPreview(context: Context, file: PreviewInfo, info: DisplayInfo, callback: AsyncCallback<void>): void

Displays the preview window based on the file preview information and floating window attributes. Calling this API repeatedly within 1 second will not take effect. This API returns the result asynchronously through a callback.

The calling app must ensure that the provided URI supports delegated access.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

file

 | 

[PreviewInfo](#section1081123302517)

 | 

Yes

 | 

File preview information. The **title** parameter is optional. If **title** is left blank, **URI** will be parsed. If **URI** cannot be parsed, the file will be marked as an unknown file.

 |
| 

info

 | 

[DisplayInfo](#section177311614561)

 | 

Yes

 | 

Modal window display information. This parameter is invalid for mobile phones and tablets.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<void>

 | 

Yes

 | 

**Callback** function. If the preview window is displayed successfully, **err** is **undefined** or **err.code** is **0**. Otherwise, **err** is an error object.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let displayInfo: filePreview.DisplayInfo = {
  x: 100,
  y: 100,
  width: 800,
  height: 800
};
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.openPreview(uiContext, fileInfo, displayInfo, (err) => {
  if (err && err.code) {
    console.error(\`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}\`);
    return;
  }
  console.info('Succeeded in opening preview');
});

#### openPreview

openPreview(context: Context, files: Array<PreviewInfo>, index?: number): Promise<void>

Displays the preview window based on the preview information of multiple files and selected file information subscripts. Calling this API repeatedly within 1 second will not take effect. This API returns the result asynchronously through a promise.

The calling app must ensure that the provided URI supports delegated access.

This API is not supported for 2-in-1 devices.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

files

 | 

Array<[PreviewInfo](#section1081123302517)\>

 | 

Yes

 | 

File preview information list.

 |
| 

index

 | 

number

 | 

No

 | 

File preview information subscripts displayed when the preview window is displayed. If this parameter is left blank, the default value **0** is used. The value is greater than or equal to **0** and less than the length of **files**.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |
| 

801

 | 

Capability not supported.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
let files: Array<filePreview.PreviewInfo> = new Array();
files.push(fileInfo);
filePreview.openPreview(uiContext, files, 0).then(() => {
  console.info('Succeeded in opening preview');
}).catch((err: BusinessError) => {
  console.error(\`Failed to open preview, err.code = ${err.code}, err.message = ${err.message}\`);
});

#### canPreview

canPreview(context: Context, uri: string): Promise<boolean>

Checks whether a file or folder can be previewed based on the URI. If the URI of a file that supports preview is passed, **true** will be returned. If the URI of a file that cannot be previewed is passed, **false** will be returned. This API returns the result asynchronously through a promise.

This API only checks whether the file exists and whether the file type is supported. When openPreview is called to view the file, the caller needs to ensure that the file supports delegated access.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

uri

 | 

string

 | 

Yes

 | 

File [URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro).

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

**Promise** object. If the URI of a file that supports preview is passed, **true** will be returned. If the URI of a file that cannot be previewed is passed, **false** will be returned.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

 // The file supports preview and exists.
let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri).then((result) => {    // **true** will be returned.
  console.info(\`Succeeded in obtaining the result of whether it can be previewed. result = ${result}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}\`);
})

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

// The file does not support preview or the file does not exist.
let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri).then((result) => {    // **false** will be returned.
  console.info(\`Succeeded in obtaining the result of whether it can be previewed. result = ${result}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}\`);
});

#### canPreview

canPreview(context: Context, uri: string, callback: AsyncCallback<boolean>): void

Checks whether a file or folder can be previewed based on the URI. If the URI of a file that supports preview is passed, **true** will be returned. If the URI of a file that cannot be previewed is passed, **false** will be returned. This API returns the result asynchronously through a callback.

This API only checks whether the file exists and whether the file type is supported. When openPreview is called to view the file, the caller needs to ensure that the file supports delegated access.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

uri

 | 

string

 | 

Yes

 | 

File [URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro).

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<boolean>

 | 

Yes

 | 

Callback function. If the URI of a file that supports preview is passed, **true** will be returned. If the URI of a file that cannot be previewed is passed, **false** will be returned.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { filePreview } from '@kit.PreviewKit';

// The file supports preview and exists.
let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri, (err, result) => {
  if (err && err.code) {
    console.error(\`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in obtaining the result of whether it can be previewed. result = ${result}\`);     // **true** will be returned.
});

import { filePreview } from '@kit.PreviewKit';

// The file does not support preview or the file does not exist.
let uri = 'file://docs/storage/Users/currentUser/Documents/9.txt';
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.canPreview(uiContext, uri, (err, result) => {
  if (err && err.code) {
    console.error(\`Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in obtaining the result of whether it can be previewed. result = ${result}\`);     // **false** will be returned.
});

#### hasDisplayed

hasDisplayed(context: Context): Promise<boolean>

Checks whether a preview window already exists. The preview window is implemented as a singleton. If the preview window has been opened and is not closed, **true** will be returned. If the preview window has not been opened or has been closed after being opened, **false** will be returned. This API returns the result asynchronously through a promise. It can take effect only after a preview window has been created. If **hasDisplayed** is called before the preview window has been created, **false** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

**Promise** object. The preview window is implemented as a singleton. If the preview window has been opened and is not closed, **true** will be returned. If the preview window has not been opened or has been closed after being opened, **false** will be returned.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

// The preview window already exists.
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext).then((result) => {    // **true** will be returned.
  console.info(\`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}\`);
});

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

 // The preview window does not exist.
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext).then((result) => {    // **false** will be returned.
  console.info(\`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}\`);
});

#### hasDisplayed

hasDisplayed(context: Context, callback: AsyncCallback<boolean>): void

Checks whether a preview window already exists. The preview window is implemented as a singleton. If the preview window has been opened and is not closed, **true** will be returned. If the preview window has not been opened or has been closed after being opened, **false** will be returned. This API returns the result asynchronously through a callback. It can take effect only after a preview window has been created. If **hasDisplayed** is called before the preview window has been created, **false** will be returned.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<boolean>

 | 

Yes

 | 

Callback function. The preview window is implemented as a singleton. If the preview window has been opened and is not closed, **true** will be returned. If the preview window has not been opened or has been closed after being opened, **false** will be returned.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { filePreview } from '@kit.PreviewKit';

// The preview window already exists.
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext, (err, result) => {
  if (err && err.code) {
    console.error(\`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}\`);     // **true** will be returned.
});

import { filePreview } from '@kit.PreviewKit';

// The preview window does not exist.
let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.hasDisplayed(uiContext, (err, result) => {
  if (err && err.code) {
    console.error(\`Failed to obtain the result of whether the preview has displayed, err.code = ${err.code}, err.message = ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in obtaining the result of whether the preview has displayed. result = ${result}\`);     // **false** will be returned.
});

#### closePreview

closePreview(context: Context): Promise<void>

Closes the preview window and takes effect only when a preview window exists. This API returns the result asynchronously through a promise. It can take effect only after a preview window has been created. If **closePreview** is called before the preview window has been created, the API call will fail.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.closePreview(uiContext).then(() => {   // Can take effect only when a preview window exists.
  console.info('Succeeded in closing preview');
}).catch((err: BusinessError) => {
  console.error(\`Failed to close preview, err.code = ${err.code}, err.message = ${err.message}\`);
});

#### closePreview

closePreview(context: Context, callback: AsyncCallback<void>): void

Closes the preview window and takes effect only when a preview window exists. This API returns the result asynchronously through a callback. It can take effect only after a preview window has been created. If **closePreview** is called before the preview window has been created, the API call will fail.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<void>

 | 

Yes

 | 

Callback function. If the preview window is closed successfully, **err** is **undefined** or **err.code** is **0**. Otherwise, **err** is an error object.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
filePreview.closePreview(uiContext, (err) => {  // Can take effect only when a preview window exists.
  if (err && err.code) {
    console.error(\`Failed to close preview, err.code = ${err.code}, err.message = ${err.message}\`);
    return;
  }
  console.info('Succeeded in closing preview');
});

#### loadData

loadData(context: Context, file: PreviewInfo): Promise<void>

Loads information about the file to be previewed. This API can take effect only when a preview window exists. If a file that can be previewed is passed, the preview page will be displayed. If a file that cannot be previewed is passed, a message will be displayed, indicating that the preview page cannot be opened. Calling this API repeatedly within 100 milliseconds will not take effect. This API returns the result asynchronously through a promise. It can take effect only after a preview window has been created. If **loadData** is called before the preview window has been created, the API call will fail.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

file

 | 

[PreviewInfo](#section1081123302517)

 | 

Yes

 | 

File preview information. The **title** parameter is optional. If **title** is left blank, **URI** will be parsed. If **URI** cannot be parsed, the file will be marked as an unknown file.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.loadData(uiContext, fileInfo).then(() => {   // Can take effect only when a preview window exists.
  console.info('Succeeded in loading data.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to load data, err.code = ${err.code}, err.message = ${err.message}\`);
});

#### loadData

loadData(context: Context, file: PreviewInfo, callback: AsyncCallback<void>): void

Loads information about the file to be previewed. This API can take effect only when a preview window exists. If a file that can be previewed is passed, the preview page will be displayed. If a file that cannot be previewed is passed, a message will be displayed, indicating that the preview page cannot be opened. Calling this API repeatedly within 100 milliseconds will not take effect. This API returns the result asynchronously through a callback. It can take effect only after a preview window has been created. If **loadData** is called before the preview window has been created, the API call will fail.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

file

 | 

[PreviewInfo](#section1081123302517)

 | 

Yes

 | 

File preview information. The **title** parameter is optional. If **title** is left blank, **URI** will be parsed. If **URI** cannot be parsed, the file will be marked as an unknown file.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<void>

 | 

Yes

 | 

Callback function. If the preview window is loaded successfully, **err** is **undefined** or **err.code** is **0**. Otherwise, **err** is an error object.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |

**Example:**

import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
filePreview.loadData(uiContext, fileInfo, (err) => {   // Can take effect only when a preview window exists.
  if (err && err.code) {
    console.error(\`Failed to load data, err.code = ${err.code}, err.message = ${err.message}\`);
    return;
  }
  console.info('Succeeded in loading data.');
});

#### loadData

loadData(context: Context, files: Array<PreviewInfo>, index?: number): Promise<void>

Loads information about the file to be previewed. This API can take effect only when a preview window exists. The preview window is displayed based on the preview information of multiple files and selected file information subscripts. This API returns the result asynchronously through a promise.

It can take effect only after a preview window has been created. If **loadData** is called before the preview window has been created, the API call will fail. This API is invalid on 2-in-1 devices. Calling this API repeatedly within 100 milliseconds will not take effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.FileManagement.FilePreview.Core

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 |  | 

Yes

 | 

Context. For details, please refer to [common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

CAUTION:

Currently, the context supports only **UIAbilityContext**.

 |
| 

files

 | 

Array<[PreviewInfo](#section1081123302517)\>

 | 

Yes

 | 

File preview information list.

 |
| 

index

 | 

number

 | 

No

 | 

File preview information subscripts displayed when the preview window is displayed. If this parameter is left blank, the default value **0** is used. The value is greater than or equal to **0** and less than the length of **files**.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error code**: For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

invalid input parameter.

 |
| 

801

 | 

Capability not supported.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { filePreview } from '@kit.PreviewKit';

let uiContext = this.getUIContext().getHostContext() as Context;
let fileInfo: filePreview.PreviewInfo = {
  title: '1.txt',
  uri: 'file://docs/storage/Users/currentUser/Documents/1.txt',
  mimeType: 'text/plain'
};
let files: Array<filePreview.PreviewInfo> = new Array();
files.push(fileInfo);
filePreview.loadData(uiContext, files, 0).then(() => {   // Can take effect only when a preview window exists.
  console.info('Succeeded in loading data.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to load data, err.code = ${err.code}, err.message = ${err.message}\`);
});
