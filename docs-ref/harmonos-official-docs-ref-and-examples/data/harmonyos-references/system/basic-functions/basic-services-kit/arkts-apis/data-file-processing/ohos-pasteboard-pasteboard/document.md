# @ohos.pasteboard (Pasteboard)

This module provides the capabilities of managing the system pasteboard to support the copy and paste functions. You can use the APIs of this module to operate pasteboard content of the plain text, HTML, URI, Want, pixel map, and other types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/JAxFm8lXQhGaYmtqVsGI9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E943DF068D659777496FD3FC51C5519FACBB53AE52CE754E0CF7CFBC5487DC7)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { pasteboard } from '@kit.BasicServicesKit';

#### Constants

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| MAX\_RECORD\_NUM7+ | number | \- | 
Maximum number of records in a **PasteData** object. In versions earlier than API version 10, the value is 512, indicating that no more records can be added once the number of records reaches 512.

Since API version 10, no limit is placed on the number of records in a **PasteData** object.

 |
| MIMETYPE\_TEXT\_HTML7+ | string | 'text/html' | MIME type of the HTML content. |
| MIMETYPE\_TEXT\_WANT7+ | string | 'text/want' | MIME type of the Want content. |
| MIMETYPE\_TEXT\_PLAIN7+ | string | 'text/plain' | MIME type of the plain text content. |
| MIMETYPE\_TEXT\_URI7+ | string | 'text/uri' | MIME type of the URI content. |
| MIMETYPE\_PIXELMAP9+ | string | 'pixelMap' | MIME type of the pixel map. |

#### ValueType9+

type ValueType = string | image.PixelMap | Want | ArrayBuffer

Enumerates the value types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Type | Description |
| :-- | :-- |
| string | The value is of the string type. |
| image.PixelMap | The value is of the [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) type. |
| Want | The value is of the [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) type. |
| ArrayBuffer | The value is of the **ArrayBuffer** type. |

#### pasteboard.createData9+

createData(mimeType: string, value: ValueType): PasteData

Creates a **PasteData** object of the specified type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | MIME type of custom data. The value can be a predefined MIME type listed in [Constants](#constants), including HTML, WANT, plain text, URI, and pixel map, or a custom MIME type. The value of **mimeType** cannot exceed 1024 bytes. |
| value | [ValueType](#valuetype9) | Yes | Content of custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteData](#pastedata) | **PasteData** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example 1**

let dataXml = new ArrayBuffer(256);
let pasteData: pasteboard.PasteData = pasteboard.createData('app/xml', dataXml);

**Example 2**

let dataText = 'hello';
let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, dataText);

#### pasteboard.createData14+

createData(data: Record<string, ValueType>): PasteData

Creates a **PasteData** object that contains multiple types of data.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [Record](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/introduction-to-arkts#object-literal)<string, [ValueType](#valuetype9)\> | Yes | 
The key of **Record** can be the MIME type corresponding to the pasteboard data, including HTML, WANT, plain text, URI, and PixelMap defined in [Constants](#constants). Alternatively, the key could be a custom MIME type, whose parameter, the length of **mimeType**, cannot exceed 1024 bytes.

The value of **Record** is the data corresponding to the MIME type specified in the key.

The first MIME type specified by the key-value in **Record** is used as the default MIME type of the first **PasteDataRecord** in the **PasteData** object. Data of non-default types can be read only by using the [getData](#getdata14) API.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteData](#pastedata) | **PasteData** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example 1**

let pasteData: pasteboard.PasteData = pasteboard.createData({
    'text/plain': 'hello',
    'app/xml': new ArrayBuffer(256),
});

**Example 2**

let record: Record<string, pasteboard.ValueType> = {};
record\[pasteboard.MIMETYPE\_TEXT\_PLAIN\] = 'hello';
record\[pasteboard.MIMETYPE\_TEXT\_URI\] = 'dataability:///com.example.myapplication1/user.txt';
let pasteData: pasteboard.PasteData = pasteboard.createData(record);

#### pasteboard.createRecord9+

createRecord(mimeType: string, value: ValueType): PasteDataRecord

Creates a **PasteDataRecord** object of the specified type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | MIME type of custom data. The value can be a predefined MIME type listed in [Constants](#constants), including HTML, WANT, plain text, URI, and pixel map, or a custom MIME type. The value of **mimeType** cannot exceed 1024 bytes. |
| value | [ValueType](#valuetype9) | Yes | Data content of the specified type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | A new paste data record of a specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example 1**

let dataXml = new ArrayBuffer(256);
let pasteDataRecord: pasteboard.PasteDataRecord = pasteboard.createRecord('app/xml', dataXml);

**Example 2**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);

#### pasteboard.getSystemPasteboard

getSystemPasteboard(): SystemPasteboard

Obtains this **SystemPasteboard** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| [SystemPasteboard](#systempasteboard) | **SystemPasteboard** object. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

#### ShareOption9+

Enumerates the pasteable ranges of pasteboard data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Value | Description |
| :-- | :-- | :-- |
| INAPP | 0 | Only intra-application pasting is allowed. |
| LOCALDEVICE | 1 | Paste is allowed in any application. |
| CROSSDEVICE(deprecated) | 2 | 
Paste is allowed in any application across devices.

This API is deprecated since API version 12 without any alternative API or method.

 |

#### pasteboard.createHtmlData(deprecated)

createHtmlData(htmlText: string): PasteData

Creates a **PasteData** object of the HTML type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/tbvirecDSiOfCzF-l3a0Tw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56F570317E709153255BE38D736762A7041F0BE3D3E9766DAD484333EE51DD4D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.createData](#pasteboardcreatedata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| htmlText | string | Yes | HTML content. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteData](#pastedata) | **PasteData** object. |

**Example**

let html = "<!DOCTYPE html>\\n" + "<html>\\n" + "<head>\\n" + "<meta charset=\\"utf-8\\">\\n" + "<title>HTML-PASTEBOARD\_HTML</title>\\n" + "</head>\\n" + "<body>\\n" + "    <h1>HEAD</h1>\\n" + "    <p></p>\\n" + "</body>\\n" + "</html>";
let pasteData: pasteboard.PasteData = pasteboard.createHtmlData(html);

#### pasteboard.createWantData(deprecated)

createWantData(want: Want): PasteData

Creates a **PasteData** object of the Want type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/rQLi1UlYQCCVGMIja4DoJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D363AE5D8ECB6CA104C06B0E0FE1EF0A60543E13F8FA5CBC1B07C00BF1DC344C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.createData](#pasteboardcreatedata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want content. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteData](#pastedata) | **PasteData** object. |

**Example**

import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let pasteData: pasteboard.PasteData = pasteboard.createWantData(object);

#### pasteboard.createPlainTextData(deprecated)

createPlainTextData(text: string): PasteData

Creates a **PasteData** object of the plain text type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/FbLBoY1iR-GRanpmzYG4Nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B06A45C7CA381EC054D523C89CDA6C88BCDFE9C3560BE76869515F55438FCD8F)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [pasteboard.createData](#pasteboardcreatedata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Plain text. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteData](#pastedata) | **PasteData** object. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');

#### pasteboard.createUriData(deprecated)

createUriData(uri: string): PasteData

Creates a **PasteData** object of the URI type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/gSDC3xELSI--CKGQnkN40A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69D61CAE66CDD5E92A0FBCB7C77C40C0D4226722DBE82FC2A19204F67FCD157A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.createData](#pasteboardcreatedata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI content. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteData](#pastedata) | **PasteData** object. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createUriData('dataability:///com.example.myapplication1/user.txt');

#### pasteboard.createHtmlTextRecord(deprecated)

createHtmlTextRecord(htmlText: string): PasteDataRecord

Creates a **PasteDataRecord** object of the HTML text type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/mup5pSwNRM6D1x0lqJA3Wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=852D01E5362F192D3BD817C2AB0C490780461B2A050DC09E54BB7292A74E6B48)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.createRecord](#pasteboardcreaterecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| htmlText | string | Yes | HTML content. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | **PasteDataRecord** object of the HTML text type. |

**Example**

let html = "<!DOCTYPE html>\\n" + "<html>\\n" + "<head>\\n" + "<meta charset=\\"utf-8\\">\\n" + "<title>HTML-PASTEBOARD\_HTML</title>\\n" + "</head>\\n" + "<body>\\n" + "    <h1>HEAD</h1>\\n" + "    <p></p>\\n" + "</body>\\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createHtmlTextRecord(html);

#### pasteboard.createWantRecord(deprecated)

createWantRecord(want: Want): PasteDataRecord

Creates a **PasteDataRecord** object of the Want type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/po1cKgzDSGq1tgvWgfdyTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22C82599E6E1A577D86EF2E7522648D771DE5C113CD275FD39871D26104D1370)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.createRecord](#pasteboardcreaterecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want content. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | New **PasteDataRecord** object of the Want type. |

**Example**

import { Want } from '@kit.AbilityKit';

let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
let record: pasteboard.PasteDataRecord = pasteboard.createWantRecord(object);

#### pasteboard.createPlainTextRecord(deprecated)

createPlainTextRecord(text: string): PasteDataRecord

Creates a **PasteDataRecord** object of the plain text type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Lk64H4hXQeKG8JxHandjbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79FFA46E5B66E5B9F13470D8492EB01DD6E18FE571F077BF73BCAE45BDB11835)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.createRecord](#pasteboardcreaterecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Plain text. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | New **PasteDataRecord** object of the plain text type. |

**Example**

let record: pasteboard.PasteDataRecord = pasteboard.createPlainTextRecord('hello');

#### pasteboard.createUriRecord(deprecated)

createUriRecord(uri: string): PasteDataRecord

Creates a **PasteDataRecord** object of the URI type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/1uoSA19dQIS3DCqucs8rtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2C8FD1B466B67D8DEEA774E0E53A0A5CDB0D78D80F7C311E0BC93CC0643F121)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.createRecord](#pasteboardcreaterecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI content. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | New **PasteDataRecord** object of the URI type. |

**Example**

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');

#### PasteDataProperty7+

Defines the properties of all data records on the pasteboard, including the timestamp, data type, pasteable range, and additional data. The defined properties can be applied to the pasteboard only with the [setProperty](#setproperty9) method.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| additions | {\[key:string\]:object} | No | No | Additional property data. It does not allow for dynamic adding of properties. Properties can be added only by re-assigning values. This parameter is left empty by default. For details, see the example of **setProperty**. |
| mimeTypes | Array<string> | Yes | No | Non-repeating data types of the data records on the pasteboard. |
| tag | string | No | No | Custom tag. This parameter is left empty by default. |
| timestamp | number | Yes | No | Timestamp when data is written to the pasteboard (unit: nanoseconds since the device is powered on). |
| localOnly | boolean | No | No | Whether the pasteboard content is for local access only. The default value is **false**. The value will be overwritten by the value of the **shareOption** attribute. You are advised to use the [ShareOption](#shareoption9) attribute instead. |
| shareOption9+ | [ShareOption](#shareoption9) | No | No | Pasteable ranges of pasteboard data. The default value is **CROSSDEVICE**. |

#### FileConflictOptions15+

Defines options for file copy conflicts.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Value | Description |
| :-- | :-- | :-- |
| OVERWRITE | 0 | Overwrites the file with the same name in the destination path. |
| SKIP | 1 | Skips the file with the same name in the destination path. If **SKIP** is set, the copied data of the skipped file is not pasted to the application. |

#### ProgressIndicator15+

Defines options for the progress indicator. You can choose whether to use the default progress indicator.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The default progress indicator is not used. |
| DEFAULT | 1 | The default progress indicator is used. |

#### ProgressInfo15+

Defines the progress information. This information is reported only when [ProgressIndicator](#progressindicator15) is set to **NONE**.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| progress | number | No | No | If the progress indicator provided by the system is not used, the system reports the progress percentage of the copy-and-paste task. |

#### ProgressListener15+

type ProgressListener = (progress: ProgressInfo) => void

Defines a listener for progress data changes. If the default progress indicator is not used, you can set this API to obtain the paste progress.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | [ProgressInfo](#progressinfo15) | Yes | Defines the progress information. This information is reported only when [ProgressIndicator](#progressindicator15) is set to **NONE**. |

#### ProgressSignal15+

Defines a function for canceling the paste task. This parameter is valid only when [ProgressIndicator](#progressindicator15) is set to **NONE**.

**System capability**: SystemCapability.MiscServices.Pasteboard

#### \[h2\]cancel15+

cancel(): void

Cancels an ongoing copy-and-paste task.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Example**

import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
@Entry
@Component
struct PasteboardTest {
 build() {
   RelativeContainer() {
     Column() {
       Column() {
         Button("Copy txt")
           .onClick(async ()=>{
              let text = "test";
              let pasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, text);
              let systemPasteboard = pasteboard.getSystemPasteboard();
              await systemPasteboard.setData(pasteData);
              let signal = new pasteboard.ProgressSignal;
              let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
                console.info('progressListener success, progress:' + progress.progress);
                signal.cancel();
              };
              let destPath: string = '/data/storage/el2/base/files/';
              let destUri : string = fileUri.getUriFromPath(destPath);
              let params: pasteboard.GetDataParams = {
                destUri: destUri,
                fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
                progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
                progressListener: progressListenerInfo,
              };
              systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
                console.info('getDataWithProgress success');
              }).catch((err: BusinessError) => {
                console.error('Failed to get PasteData. Cause: ' + err.message);
              })
          })
        }
      }
    }
  }
}

#### GetDataParams15+

Obtains parameters when an application uses the file copy capability provided by the pasteboard, including the destination path, file conflict options, and progress indicator types.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| destUri | string | No | Yes | Destination path for copying files. If file processing is not supported, this parameter is not required. If the application involves complex file processing policies or needs to distinguish file multipathing storage, you are advised not to set this parameter but let the application copy files by itself. This parameter is left empty by default. |
| fileConflictOptions | [FileConflictOptions](#fileconflictoptions15) | No | Yes | File conflict options for a copy-and-paste task. The default value is **OVERWRITE**. |
| progressIndicator | [ProgressIndicator](#progressindicator15) | No | No | Progress indicator options. You can choose whether to use the default progress indicator. |
| progressListener | [ProgressListener](#progresslistener15) | No | Yes | Defines a listener for progress data changes. If the default progress indicator is not used, you can set this type to obtain the paste progress. This parameter is left empty by default. |
| progressSignal | [ProgressSignal](#progresssignal15) | No | Yes | Function for canceling the paste task. This parameter is valid only when [ProgressIndicator](#progressindicator15) is set to **NONE**. This parameter is left empty by default. |

#### PasteDataRecord7+

Provides **PasteDataRecord** APIs. A **PasteDataRecord** is an abstract definition of the content on the pasteboard. The pasteboard content consists of one or more plain text, HTML, URI, or Want records.

#### \[h2\]Attributes

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| htmlText | string | Yes | No | HTML content. |
| want | [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | No | Want content. |
| mimeType | string | Yes | No | Default data type. |
| plainText | string | Yes | No | Plain text. |
| uri | string | Yes | No | URI content. |
| pixelMap9+ | [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | No | Pixel map. |
| data9+ | {\[mimeType: string\]: ArrayBuffer} | Yes | No | Content of custom data. |

#### \[h2\]toPlainText9+

toPlainText(): string

Forcibly converts HTML, plain, and URI content in a **PasteDataRecord** to the plain text.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| string | Plain text. |

**Example**

let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_HTML, '<html>hello</html>');
let text: string = record.toPlainText();
console.info(\`Succeeded in converting to text. Text: ${text}\`);

#### \[h2\]addEntry14+

addEntry(type: string, value: ValueType): void

Adds custom data of an extra type to **PasteDataRecord**. The MIME type added using this method is not the default type of **Record**. You can only use the [getData](#getdata14) API to read the corresponding data.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | MIME type of custom data. The value can be a predefined MIME type listed in [Constants](#constants), including HTML, WANT, plain text, URI, and pixel map, or a custom MIME type. The value of **mimeType** cannot exceed 1024 bytes. |
| value | [ValueType](#valuetype9) | Yes | Content of custom data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

let html = "<!DOCTYPE html>\\n" + "<html>\\n" + "<head>\\n" + "<meta charset=\\"utf-8\\">\\n" + "<title>HTML-PASTEBOARD\_HTML</title>\\n" + "</head>\\n" + "<body>\\n" + "    <h1>HEAD</h1>\\n" + "    <p></p>\\n" + "</body>\\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE\_TEXT\_HTML, html);

#### \[h2\]getValidTypes14+

getValidTypes(types: Array<string>): Array<string>

Obtains the intersection of the input MIME type and the MIME type of the pasteboard data.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| types | Array<string> | Yes | List of the MIME types. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Intersection of the input MIME type and the MIME type of the pasteboard data obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

let html = "<!DOCTYPE html>\\n" + "<html>\\n" + "<head>\\n" + "<meta charset=\\"utf-8\\">\\n" + "<title>HTML-PASTEBOARD\_HTML</title>\\n" + "</head>\\n" + "<body>\\n" + "    <h1>HEAD</h1>\\n" + "    <p></p>\\n" + "</body>\\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE\_TEXT\_HTML, html);
let types: string\[\] = record.getValidTypes(\[
    pasteboard.MIMETYPE\_TEXT\_PLAIN,
    pasteboard.MIMETYPE\_TEXT\_HTML,
    pasteboard.MIMETYPE\_TEXT\_URI,
    pasteboard.MIMETYPE\_TEXT\_WANT,
    pasteboard.MIMETYPE\_PIXELMAP
\]);

#### \[h2\]getData14+

getData(type: string): Promise<ValueType>

Obtains custom data of the specified MIME type from **PasteDataRecord**.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | MIME type, which cannot exceed 1024 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ValueType](#valuetype9)\> | 
Promise used to return the custom data of the specified MIME type.

If **PasteDataRecord** contains data of multiple MIME types, the non-**PasteDataRecord** data of the default MIME type can be obtained only through this API.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let html = "<!DOCTYPE html>\\n" + "<html>\\n" + "<head>\\n" + "<meta charset=\\"utf-8\\">\\n" + "<title>HTML-PASTEBOARD\_HTML</title>\\n" + "</head>\\n" + "<body>\\n" + "    <h1>HEAD</h1>\\n" + "    <p></p>\\n" + "</body>\\n" + "</html>";
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_URI, 'dataability:///com.example.myapplication1/user.txt');
record.addEntry(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
record.addEntry(pasteboard.MIMETYPE\_TEXT\_HTML, html);
record.getData(pasteboard.MIMETYPE\_TEXT\_PLAIN).then((value: pasteboard.ValueType) => {
    let textPlainContent = value as string;
    console.info('Success to get text/plain value. value is: ' + textPlainContent);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/plain value. Cause: ' + err.message);
});
record.getData(pasteboard.MIMETYPE\_TEXT\_URI).then((value: pasteboard.ValueType) => {
    let uri = value as string;
    console.info('Success to get text/uri value. value is: ' + uri);
}).catch((err: BusinessError) => {
    console.error('Failed to get text/uri value. Cause: ' + err.message);
});

#### \[h2\]convertToText(deprecated)

convertToText(callback: AsyncCallback<string>): void

Forcibly converts the content in a **PasteData** object to text. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/pdR47rFHSwGyO-uZ8dErMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2001793560DB9AA1BD7A99160A761F0967AAD66149D72C1B03224B867BF50896)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [toPlainText](#toplaintext9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the text obtained from the conversion. Otherwise, **err** is error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText((err: BusinessError, data: string) => {
    if (err) {
        console.error(\`Failed to convert to text. Cause: ${err.message}\`);
        return;
    }
    console.info(\`Succeeded in converting to text. Data: ${data}\`);
});

#### \[h2\]convertToText(deprecated)

convertToText(): Promise<string>

Forcibly converts the content in a **PasteData** object to text. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/OPjGZYDfTtKucg-rpGOK2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=489AAA7461E69B437ADB73B244D637B577E5FA4C13DF96A984E83C9713315101)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [toPlainText](#toplaintext9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the text obtained from the conversion. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
record.convertToText().then((data: string) => {
    console.info(\`Succeeded in converting to text. Data: ${data}\`);
}).catch((err: BusinessError) => {
    console.error(\`Failed to convert to text. Cause: ${err.message}\`);
});

#### PasteData

Implements a **PasteData** object. Paste data contains one or more data records ([PasteDataRecord](#pastedatarecord7)) and property description objects ([PasteDataProperty](#pastedataproperty7)).

Before calling any API in **PasteData**, you must use **[createData()](#pasteboardcreatedata9)** or **[getData()](#getdata9)** to create a **PasteData** object.

**System capability**: SystemCapability.MiscServices.Pasteboard

#### \[h2\]getPrimaryText

getPrimaryText(): string

Obtains the plain text of the primary record.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| string | Plain text. If the **PasteData** object does not contain plain text, **undefined** is returned by default. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});

#### \[h2\]getPrimaryHtml7+

getPrimaryHtml(): string

Obtains the HTML content of the primary record.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| string | HTML content. If the **PasteData** object does not contain HTML content, **undefined** is returned by default. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let htmlText: string = pasteData.getPrimaryHtml();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});

#### \[h2\]getPrimaryWant7+

getPrimaryWant(): Want

Obtains the **Want** object of the primary record.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Want object. If the **PasteData** object does not contain the **Want** object, **undefined** is returned by default. |

**Example**

import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let want: Want = pasteData.getPrimaryWant();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});

#### \[h2\]getPrimaryUri7+

getPrimaryUri(): string

Obtains the URI of the primary record.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| string | URI content. If the **PasteData** object does not contain the URI, **undefined** is returned by default. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let uri: string = pasteData.getPrimaryUri();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});

#### \[h2\]getPrimaryPixelMap9+

getPrimaryPixelMap(): image.PixelMap

Obtains the pixel map of the primary record.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Pixel map. If the **PasteData** object does not contain the pixel map, **undefined** is returned by default. |

**Example**

import { image } from '@kit.ImageKit';

let buffer = new ArrayBuffer(128);
let realSize: image.Size = { height: 3, width: 5 };
let opt: image.InitializationOptions = {
    size: realSize,
    pixelFormat: 3,
    editable: true,
    alphaType: 1,
    scaleMode: 1
};
image.createPixelMap(buffer, opt).then((pixelMap: image.PixelMap) => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_PIXELMAP, pixelMap);
    let PixelMap: image.PixelMap = pasteData.getPrimaryPixelMap();
});

#### \[h2\]addRecord7+

addRecord(record: PasteDataRecord): void

Adds a data record to this pasteboard, and adds its type to **mimeTypes** in [PasteDataProperty](#pastedataproperty7). The parameters cannot be empty. Otherwise, the operation fails.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| record | [PasteDataRecord](#pastedatarecord7) | Yes | Record to add. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_URI, 'dataability:///com.example.myapplication1/user.txt');
let textRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let html: string = "<!DOCTYPE html>\\n" + "<html>\\n" + "<head>\\n" + "<meta charset=\\"utf-8\\">\\n" + "<title>HTML-PASTEBOARD\_HTML</title>\\n" + "</head>\\n" + "<body>\\n" + "    <h1>HEAD</h1>\\n" + "    <p></p>\\n" + "</body>\\n" + "</html>";
let htmlRecord: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_HTML, html);
pasteData.addRecord(textRecord);
pasteData.addRecord(htmlRecord);

#### \[h2\]addRecord9+

addRecord(mimeType: string, value: ValueType): void

Adds a data record to this pasteboard, and adds its type to **mimeTypes** in [PasteDataProperty](#pastedataproperty7). The parameters cannot be empty. Otherwise, the operation fails.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | MIME type of pasteboard data. The length cannot exceed 1024 bytes. |
| value | [ValueType](#valuetype9) | Yes | Data content. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_URI, 'dataability:///com.example.myapplication1/user.txt');
let dataXml = new ArrayBuffer(256);
pasteData.addRecord('app/xml', dataXml);

#### \[h2\]getMimeTypes7+

getMimeTypes(): Array<string>

Obtains MIME types of [PasteDataProperty](#pastedataproperty7) on the pasteboard. If an exception occurs during API invoking, **undefined** is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Non-repeating data types of the data records on the pasteboard. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let types: string\[\] = pasteData.getMimeTypes();

#### \[h2\]getPrimaryMimeType7+

getPrimaryMimeType(): string

Obtains the data type of the primary record in this pasteboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| string | Data type of the primary record. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let type: string = pasteData.getPrimaryMimeType();

#### \[h2\]getProperty7+

getProperty(): PasteDataProperty

Obtains the property of the pasteboard data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataProperty](#pastedataproperty7) | Property of the pasteboard data. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let property: pasteboard.PasteDataProperty = pasteData.getProperty();

#### \[h2\]setProperty9+

setProperty(property: PasteDataProperty): void

Sets a [PasteDataProperty](#pastedataproperty7) object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| property | [PasteDataProperty](#pastedataproperty7) | Yes | Property of the pasteboard data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

type AdditionType = Record<string, Record<string, Object>>;

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_HTML, 'application/xml');
let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
prop.shareOption = pasteboard.ShareOption.INAPP;
// Note that attributes cannot be added to additions. Attributes can be added only by re-assigning values.
prop.additions = { 'TestOne': { 'Test': 123 }, 'TestTwo': { 'Test': 'additions' } } as AdditionType;
prop.tag = 'TestTag';
pasteData.setProperty(prop);

The **localOnly** and **shareOption** attributes of [PasteDataProperty](#pastedataproperty7) are mutually exclusive. The **shareOption** attribute is prioritized, and its value affects the value of **localOnly**.

(async () => {
    let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
    let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
    prop.shareOption = pasteboard.ShareOption.INAPP;
    prop.localOnly = false;
    pasteData.setProperty(prop);
    const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });

    prop.shareOption = pasteboard.ShareOption.LOCALDEVICE;
    prop.localOnly = false;
    pasteData.setProperty(prop);

    await systemPasteboard.setData(pasteData).then(async () => {
        console.info('Succeeded in setting PasteData.');
        await systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
            let prop: pasteboard.PasteDataProperty = pasteData.getProperty();
            prop.localOnly; // true
        });
    });
})

#### \[h2\]getRecord9+

getRecord(index: number): PasteDataRecord

Obtains the record with a specific index from the pasteboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the target record. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | Record with the specified index. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900001 | The index is out of the record. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecord(0);

#### \[h2\]getRecordCount7+

getRecordCount(): number

Obtains the number of records in the pasteboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of records. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let count: number = pasteData.getRecordCount();

#### \[h2\]getTag7+

getTag(): string

Obtains the custom tag from the pasteboard. If no custom tag is set, null is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| string | Custom tag. If no custom tag is set, null is returned. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let tag: string = pasteData.getTag();

#### \[h2\]hasType9+

hasType(mimeType: string): boolean

Checks whether the pasteboard contains data of the specified type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | Type of the data to query. The value can be a predefined type listed in Constants(#constants), including HTML, WANT, plain text, URI, and pixel map, or a custom MIME type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the specified data type exists; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let hasType: boolean = pasteData.hasType(pasteboard.MIMETYPE\_TEXT\_PLAIN);

#### \[h2\]removeRecord9+

removeRecord(index: number): void

Removes the record with a specific index from the pasteboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Specified index. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900001 | The index is out of the record. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
pasteData.removeRecord(0);

#### \[h2\]replaceRecord9+

replaceRecord(index: number, record: PasteDataRecord): void

Replaces the record with a specific index from the pasteboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Specified index. |
| record | [PasteDataRecord](#pastedatarecord7) | Yes | New record. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900001 | The index is out of the record. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
let record: pasteboard.PasteDataRecord = pasteboard.createRecord(pasteboard.MIMETYPE\_TEXT\_URI, 'file://com.example.myapplication1/data/storage/el2/base/files/file.txt');
pasteData.replaceRecord(0, record);

#### \[h2\]pasteStart12+

pasteStart(): void

Notifies the clipboard service to retain the cross-device channel before reading data from the clipboard.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    pasteData.pasteStart();
    console.info(\`using data: ${pasteData.getPrimaryText()}\`);
    pasteData.pasteComplete();
});

#### \[h2\]pasteComplete12+

pasteComplete(): void

Notifies the clipboard service that the paste is complete.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    pasteData.pasteStart();
    console.info(\`using data: ${pasteData.getPrimaryText()}\`);
    pasteData.pasteComplete();
});

#### \[h2\]addHtmlRecord(deprecated)

addHtmlRecord(htmlText: string): void

Adds an HTML record to this pasteboard, and adds **MIMETYPE\_TEXT\_HTML** to **mimeTypes** in [PasteDataProperty](#pastedataproperty7). The parameters cannot be empty. Otherwise, the operation fails.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/X6Up1ISHTmC8SJgjl6eS_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E3E8EA116951FD3B1560C3DC96DD68CF0873EACE4CFC7E35A0AE76A3384025A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [addRecord](#addrecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| htmlText | string | Yes | HTML content. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let html: string = "<!DOCTYPE html>\\n" + "<html>\\n" + "<head>\\n" + "<meta charset=\\"utf-8\\">\\n" + "<title>HTML-PASTEBOARD\_HTML</title>\\n" + "</head>\\n" + "<body>\\n" + "    <h1>HEAD</h1>\\n" + "    <p></p>\\n" + "</body>\\n" + "</html>";
pasteData.addHtmlRecord(html);

#### \[h2\]addWantRecord(deprecated)

addWantRecord(want: Want): void

Adds a Want record to this pasteboard, and adds **MIMETYPE\_TEXT\_WANT** to **mimeTypes** in [PasteDataProperty](#pastedataproperty7). The parameters cannot be empty. Otherwise, the operation fails.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/o6RuTdTAR2yz7N63oFsxlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77936350F95118D07E5FD4892AF319C3DCD812E037711324A9F0BFB735F8C857)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [addRecord](#addrecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want object. |

**Example**

import { Want } from '@kit.AbilityKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let object: Want = {
    bundleName: "com.example.aafwk.test",
    abilityName: "com.example.aafwk.test.TwoAbility"
};
pasteData.addWantRecord(object);

#### \[h2\]addTextRecord(deprecated)

addTextRecord(text: string): void

Adds a plain text record to this pasteboard, and adds **MIMETYPE\_TEXT\_PLAIN** to **mimeTypes** in [PasteDataProperty](#pastedataproperty7). The parameters cannot be empty. Otherwise, the operation fails.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/CG_qoCNfQUy8iUqnERUzTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E4931026091B168D6CACA79E9044A2D0DE0CD0C0CA0629D1732100D6EF35734)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [addRecord](#addrecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Plain text. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addTextRecord('good');

#### \[h2\]addUriRecord(deprecated)

addUriRecord(uri: string): void

Adds a URI record to this pasteboard, and adds **MIMETYPE\_TEXT\_URI** to **mimeTypes** in [PasteDataProperty](#pastedataproperty7). The parameters cannot be empty. Otherwise, the operation fails.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/_4-t2U8eRLayCCAgeuiurA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3480B653210799A39FCF9E08658321DA5587EAF4D60CB173604E33A66A58AC0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [addRecord](#addrecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI content. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
pasteData.addUriRecord('dataability:///com.example.myapplication1/user.txt');

#### \[h2\]getRecordAt(deprecated)

getRecordAt(index: number): PasteDataRecord

Obtains the record with a specific index from the pasteboard.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/JmKSxfS6STSDOHFl0NPr4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC341911EEEFE63392B3586E612D7E2A781445A64CA08E32040297F948E82BDD)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getRecord](#getrecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the target record. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteDataRecord](#pastedatarecord7) | Record with the specified index. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteData.getRecordAt(0);

#### \[h2\]hasMimeType(deprecated)

hasMimeType(mimeType: string): boolean

Checks whether the pasteboard contains data of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/5K_n3LUGScOe5RcQepLaRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26D0B34B64354DC52A6E9436AF1837103ED0E2BDD6FFA6F96943B984AED65DCB)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [hasType](#hastype9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | Type of the data to query. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the specified data type exists; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let hasType: boolean = pasteData.hasMimeType(pasteboard.MIMETYPE\_TEXT\_PLAIN);

#### \[h2\]removeRecordAt(deprecated)

removeRecordAt(index: number): boolean

Removes the record with a specific index from the pasteboard.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Y8FldBWsR26UsLEUezwM8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=186744928EA18770A7D2B1B66FC7B01CFF8C127B093C46BE4CE5B8DF44FED635)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [removeRecord](#removerecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Specified index. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let isRemove: boolean = pasteData.removeRecordAt(0);

#### \[h2\]replaceRecordAt(deprecated)

replaceRecordAt(index: number, record: PasteDataRecord): boolean

Replaces the record with a specific index from the pasteboard.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/3Qqyr-mKSzy25CcZbKJ9XA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16273408BABCB8ADFB2FF34536C2A012945F27EF0C5E75AB8AFC92A494140E0F)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [replaceRecord](#replacerecord9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Specified index. |
| record | [PasteDataRecord](#pastedatarecord7) | Yes | New record. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('hello');
let record: pasteboard.PasteDataRecord = pasteboard.createUriRecord('dataability:///com.example.myapplication1/user.txt');
let isReplace: boolean = pasteData.replaceRecordAt(0, record);

#### SystemPasteboard

Provides **SystemPasteboard** APIs.

Before calling any **SystemPasteboard** API, you must obtain a **SystemPasteboard** object using [getSystemPasteboard](#pasteboardgetsystempasteboard).

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();

#### \[h2\]on('update')7+

on(type: 'update', callback: () =>void): void

Subscribes to the content change event of the system pasteboard.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'update'** indicates changes in the pasteboard content. |
| callback | function | Yes | Callback invoked when the pasteboard content changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.on('update', listener);

#### \[h2\]off('update')7+

off(type: 'update', callback?: () =>void): void

Unsubscribes from the system pasteboard content change event.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'update'** indicates changes in the pasteboard content. |
| callback | function | No | Callback invoked when the pasteboard content changes. If this parameter is not specified, listening will be disabled for all callbacks registered by the current application. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The system pasteboard has changed.');
};
systemPasteboard.off('update', listener);

#### \[h2\]clearData9+

clearData(callback: AsyncCallback<void>): void

Clears the system pasteboard. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData((err, data) => {
    if (err) {
        console.error(\`Failed to clear the pasteboard. Cause: ${err.message}\`);
        return;
    }
    console.info('Succeeded in clearing the pasteboard.');
});

#### \[h2\]clearData9+

clearData(): Promise<void>

Clears the system pasteboard. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clearData().then((data: void) => {
    console.info('Succeeded in clearing the pasteboard.');
}).catch((err: BusinessError) => {
    console.error(\`Failed to clear the pasteboard. Cause: ${err.message}\`);
});

#### \[h2\]setData9+

setData(data: PasteData, callback: AsyncCallback<void>): void

Writes a **PasteData** object to the pasteboard. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | Yes | **PasteData** object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});

#### \[h2\]setData9+

setData(data: PasteData): Promise<void>

Writes a **PasteData** object to the pasteboard. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | Yes | **PasteData** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error('Failed to set PasteData. Cause: ' + err.message);
});

#### \[h2\]getData9+

getData(callback: AsyncCallback<PasteData>): void

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PasteData](#pastedata)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the system pasteboard data. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    let text: string = pasteData.getPrimaryText();
});

#### \[h2\]getData9+

getData(): Promise<PasteData>

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PasteData](#pastedata)\> | Promise used to return the system pasteboard data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 27787277 | Another copy or paste operation is in progress. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});

#### \[h2\]hasData9+

hasData(callback: AsyncCallback<boolean>): void

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(\`Failed to check the PasteData. Cause: ${err.message}\`);
        return;
    }
    console.info(\`Succeeded in checking the PasteData. Data: ${data}\`);
});

#### \[h2\]hasData9+

hasData(): Promise<boolean>

Checks whether the system pasteboard contains data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasData().then((data: boolean) => {
    console.info(\`Succeeded in checking the PasteData. Data: ${data}\`);
}).catch((err: BusinessError) => {
    console.error(\`Failed to check the PasteData. Cause: ${err.message}\`);
});

#### \[h2\]clear(deprecated)

clear(callback: AsyncCallback<void>): void

Clears the system pasteboard. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/nVjRrmh6SfuSaL2iM6Wt_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C74AEBB2009AD9DAA338A9D05DDFBF0C18F35806A3BE6967C34AAF7E7E19C40D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [pasteboard.clearData](#cleardata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear((err, data) => {
    if (err) {
        console.error(\`Failed to clear the PasteData. Cause: ${err.message}\`);
        return;
    }
    console.info('Succeeded in clearing the PasteData.');
});

#### \[h2\]clear(deprecated)

clear(): Promise<void>

Clears the system pasteboard. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/4HlOz31ySpy01qf5Y-r7ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AB02461AA0C5FC06196C51857FD85877453041D46743A7FE2F2AA9B8590040B)

This API is supported since API version 7 and deprecated since API version 9. Use [pasteboard.clearData](#cleardata9-1) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.clear().then((data) => {
    console.info('Succeeded in clearing the PasteData.');
}).catch((err: BusinessError) => {
    console.error(\`Failed to clear the PasteData. Cause: ${err.message}\`);
});

#### \[h2\]getPasteData(deprecated)

getPasteData(callback: AsyncCallback<PasteData>): void

Obtains a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Abr6Zx3nQRuhfsAZkTimzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11C2F60934ADBF6ABF9C1945AF9D65ABCB592F1CACD6E03EE9530C73EF1BA39A)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getData](#getdata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PasteData](#pastedata)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the system pasteboard data. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData((err: BusinessError, pasteData: pasteboard.PasteData) => {
    if (err) {
        console.error('Failed to get PasteData. Cause: ' + err.message);
        return;
    }
    let text: string = pasteData.getPrimaryText();
});

#### \[h2\]getPasteData(deprecated)

getPasteData(): Promise<PasteData>

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/T4sJXInPRb-QXOBFAyTDfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40EAAA7CCC8BC53D956CEDE41E7B58F0B0237641A9484570B4414835F7A87CEE)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getData](#getdata9-1) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PasteData](#pastedata)\> | Promise used to return the system pasteboard data. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getPasteData().then((pasteData: pasteboard.PasteData) => {
    let text: string = pasteData.getPrimaryText();
}).catch((err: BusinessError) => {
    console.error('Failed to get PasteData. Cause: ' + err.message);
});

#### \[h2\]hasPasteData(deprecated)

hasPasteData(callback: AsyncCallback<boolean>): void

Checks whether the system pasteboard contains data. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/gsiWbHY7R3-tYu1Hc7JupA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9143E8133C6BAEADCD6A9C29280FB9FD263F8CBA7B3E97250757EB475591973A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [hasData](#hasdata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(\`Failed to check the PasteData. Cause: ${err.message}\`);
        return;
    }
    console.info(\`Succeeded in checking the PasteData. Data: ${data}\`);
});

#### \[h2\]hasPasteData(deprecated)

hasPasteData(): Promise<boolean>

Checks whether the system pasteboard contains data. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ovrQIHOLQZWWDCt_V8ILkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEF53F1D6C0E79C18BDCA94A6304A33B1FDB90905A24745CA610CC3B03A1A907)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [hasData](#hasdata9-1) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.hasPasteData().then((data: boolean) => {
    console.info(\`Succeeded in checking the PasteData. Data: ${data}\`);
}).catch((err: BusinessError) => {
    console.error(\`Failed to check the PasteData. Cause: ${err.message}\`);
});

#### \[h2\]setPasteData(deprecated)

setPasteData(data: PasteData, callback: AsyncCallback<void>): void

Writes a **PasteData** object to the pasteboard. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/XVgwxx-pRLefyKZ3gsf3Gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C3DCFF1111CB6D99D17B3F822A83B9171666D0574B5EC36E0761EAACDA2DC3B)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setData](#setdata9) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | Yes | **PasteData** object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData, (err, data) => {
    if (err) {
        console.error('Failed to set PasteData. Cause: ' + err.message);
        return;
    }
    console.info('Succeeded in setting PasteData.');
});

#### \[h2\]setPasteData(deprecated)

setPasteData(data: PasteData): Promise<void>

Writes a **PasteData** object to the pasteboard. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/6BciNPYlQb-htnsa-Z-kkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5690F1C7A739A9FE84A14B5596320E1779801F844A0396D20A4B8B96648C1125)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [setData](#setdata9-1) instead.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | Yes | **PasteData** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setPasteData(pasteData).then((data: void) => {
    console.info('Succeeded in setting PasteData.');
}).catch((err: BusinessError) => {
    console.error('Failed to set PasteData. Cause: ' + err.message);
});

#### \[h2\]isRemoteData11+

isRemoteData(): boolean

Checks whether the data in the pasteboard is from another device.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data in the pasteboard is from another device; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.isRemoteData();
    console.info(\`Succeeded in checking the RemoteData. Result: ${result}\`);
} catch (err) {
    console.error('Failed to check the RemoteData. Cause:' + err.message);
};

#### \[h2\]getDataSource11+

getDataSource(): string

Obtains the name of the application that provides data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| string | Application name. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: string = systemPasteboard.getDataSource();
    console.info(\`Succeeded in getting DataSource. Result: ${result}\`);
} catch (err) {
    console.error('Failed to get DataSource. Cause:' + err.message);
};

#### \[h2\]hasDataType11+

hasDataType(mimeType: string): boolean

Checks whether the pasteboard contains data of the specified type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | string | Yes | Data type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the pasteboard contains data of the specified type; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE\_TEXT\_PLAIN);
    console.info(\`Succeeded in checking the DataType. Result: ${result}\`);
} catch (err) {
    console.error('Failed to check the DataType. Cause:' + err.message);
};

#### \[h2\]clearDataSync11+

clearDataSync(): void

Clears the system pasteboard. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.clearDataSync();
    console.info('Succeeded in clearing the pasteboard.');
} catch (err) {
    console.error('Failed to clear the pasteboard. Cause:' + err.message);
};

#### \[h2\]getDataSync11+

getDataSync(): PasteData

Reads data in the system pasteboard. This API returns the result synchronously.

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| [PasteData](#pastedata) | Data in the system pasteboard. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: pasteboard.PasteData = systemPasteboard.getDataSync();
    console.info('Succeeded in getting PasteData.');
} catch (err) {
    console.error('Failed to get PasteData. Cause:' + err.message);
};

#### \[h2\]setDataSync11+

setDataSync(data: PasteData): void

Writes data to the system pasteboard. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [PasteData](#pastedata) | Yes | Data to be written to the pasteboard. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**Example**

let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, 'hello');
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setDataSync(pasteData);
    console.info('Succeeded in setting PasteData.');
} catch (err) {
    console.error('Failed to set PasteData. Cause:' + err.message);
};

#### \[h2\]hasDataSync11+

hasDataSync(): boolean

Checks whether the system pasteboard contains data. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Callback used to return the result. Returns **true** if the system pasteboard contains data; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 12900005 | Excessive processing time for internal data. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: boolean = systemPasteboard.hasDataSync();
    console.info(\`Succeeded in checking the PasteData. Result: ${result}\`);
} catch (err) {
    console.error('Failed to check the PasteData. Cause:' + err.message);
};

#### \[h2\]getUnifiedData12+

getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>

Obtains a **PasteData** object from the pasteboard. This API uses a promise to return the result.

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[unifiedDataChannel.UnifiedData](../../../../../../application-framework/arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddata)\> | Promise used to return the system pasteboard data. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 27787277 | Another copy or paste operation is in progress. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getUnifiedData().then((data) => {
    let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
    for (let j = 0; j < records.length; j++) {
        if (records\[j\].getType() === uniformTypeDescriptor.UniformDataType.PLAIN\_TEXT) {
            let text = records\[j\].getValue() as uniformDataStruct.PlainText;
            console.info(\`${j + 1}.${text.textContent}\`);
        }
    }
}).catch((err: BusinessError) => {
    console.error('Failed to get UnifiedData. Cause: ' + err.message);
});

#### \[h2\]getUnifiedDataSync12+

getUnifiedDataSync(): unifiedDataChannel.UnifiedData

Reads data in the system pasteboard. This API returns the result synchronously.

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| [unifiedDataChannel.UnifiedData](../../../../../../application-framework/arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddata) | Data in the system pasteboard. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 12900005 | Excessive processing time for internal data. |

**Example**

import { unifiedDataChannel } from '@kit.ArkData';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result: unifiedDataChannel.UnifiedData = systemPasteboard.getUnifiedDataSync();
    console.info('Succeeded in getting UnifiedData.');
} catch (err) {
    console.error('Failed to get UnifiedData. Cause:' + err.message);
};

#### \[h2\]setUnifiedData12+

setUnifiedData(data: unifiedDataChannel.UnifiedData): Promise<void>

Writes a **PasteData** object to the pasteboard. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [unifiedDataChannel.UnifiedData](../../../../../../application-framework/arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddata) | Yes | Data to be written to the pasteboard. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 27787277 | Another copy or paste operation is in progress. |
| 27787278 | Replication is prohibited. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { unifiedDataChannel, uniformDataStruct, uniformTypeDescriptor } from '@kit.ArkData';

let plainText : uniformDataStruct.PlainText = {
    uniformDataType: uniformTypeDescriptor.UniformDataType.PLAIN\_TEXT,
    textContent : 'PLAINTEXT\_CONTENT',
    abstract : 'PLAINTEXT\_ABSTRACT',
}
let record = new unifiedDataChannel.UnifiedRecord(uniformTypeDescriptor.UniformDataType.PLAIN\_TEXT, plainText);
let data = new unifiedDataChannel.UnifiedData();
data.addRecord(record);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.setUnifiedData(data).then((data: void) => {
    console.info('Succeeded in setting UnifiedData.');
}).catch((err: BusinessError) => {
    console.error('Failed to setUnifiedData. Cause: ' + err.message);
});

#### \[h2\]setUnifiedDataSync12+

setUnifiedDataSync(data: unifiedDataChannel.UnifiedData): void

Writes data to the system pasteboard. This API returns the result synchronously.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [unifiedDataChannel.UnifiedData](../../../../../../application-framework/arkdata/arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddata) | Yes | Data to be written to the pasteboard. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 12900005 | Excessive processing time for internal data. |

**Example**

import { unifiedDataChannel } from '@kit.ArkData';

let plainTextData = new unifiedDataChannel.UnifiedData();
let plainText = new unifiedDataChannel.PlainText();
plainText.details = {
    Key: 'delayPlaintext',
    Value: 'delayPlaintext',
};
plainText.textContent = 'delayTextContent';
plainText.abstract = 'delayTextContent';
plainTextData.addRecord(plainText);

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    systemPasteboard.setUnifiedDataSync(plainTextData);
    console.info('Succeeded in setting UnifiedData.');
} catch (err) {
    console.error('Failed to set UnifiedData. Cause:' + err.message);
};

#### \[h2\]setAppShareOptions14+

setAppShareOptions(shareOptions: ShareOption): void

Sets pasteable range of pasteboard data for applications.

**Required permissions**: ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shareOptions | [ShareOption](#shareoption9) | Yes | Pasteable range. Only **pasteboard.ShareOption.INAPP** is allowed. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12900006 | Settings already exist. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.setAppShareOptions(pasteboard.ShareOption.INAPP);
  console.info('Set app share options success.');
} catch (error) {
  console.error(\`Set app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.\`);
}

#### \[h2\]removeAppShareOptions14+

removeAppShareOptions(): void

Deletes the global pasteable range of the application.

**Required permissions**: ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION

**System capability**: SystemCapability.MiscServices.Pasteboard

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
  systemPasteboard.removeAppShareOptions();
  console.info('Remove app share options success.');
} catch (error) {
  console.error(\`Remove app share options failed, errorCode: ${error.code}, errorMessage: ${error.message}.\`);
}

#### \[h2\]Pattern13+

Describes the modes supported by the pasteboard.

**System capability**: SystemCapability.MiscServices.Pasteboard

| Name | Value | Description |
| :-- | :-- | :-- |
| URL | 0 | URL. |
| NUMBER | 1 | Number. |
| EMAIL\_ADDRESS | 2 | Email address. |

#### \[h2\]detectPatterns13+

detectPatterns(patterns: Array<Pattern>): Promise<Array<Pattern>>

Detects [patterns](#pattern13) on the local pasteboard. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| patterns | [Array<Pattern>](#pattern13) | Yes | Pattern to be detected in the pasteboard. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<Pattern>> | Promise used to return the detected pattern. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. 3. Parameter verification failed. |

**Example**

import { pasteboard } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let patterns: Array<pasteboard.Pattern> = \[pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL\_ADDRESS\];

systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
    if (patterns.sort().join('')==data.sort().join('')) {
      console.info('All needed patterns detected, next get data');
      try {
        let result: pasteboard.PasteData = systemPasteboard.getDataSync();
        console.info('Succeeded in getting PasteData.');
      } catch (err) {
        console.error('Failed to get PasteData. Cause:' + err.message);
      };
    } else {
      console.info("Not all needed patterns detected, no need to get data.");
    }
});

#### \[h2\]getMimeTypes14+

getMimeTypes(): Promise<Array<string>>

Obtains the MIME type from the pasteboard. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the read MIME type. |

**Example**

import { pasteboard, BusinessError } from '@kit.BasicServicesKit'

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
systemPasteboard.getMimeTypes().then((data: Array<String>) => {
    console.info('Succeeded in getting mimeTypes. mimeTypes: ' + data.sort().join(','));
}).catch((err: BusinessError) => {
    console.error('Failed to get mimeTypes. Cause:' + err.message);
});

#### \[h2\]getDataWithProgress15+

getDataWithProgress(params: GetDataParams): Promise<PasteData>

Obtains the pasteboard data and progress. This API uses a promise to return the result. Folders cannot be copied.

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| params | [GetDataParams](#getdataparams15) | Yes | Parameters required when an application uses the file copy capability provided by the pasteboard, including the destination path, file conflict options, and progress indicator types. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PasteData](#pastedata)\> | Promise used to return the system pasteboard data. |

**Error codes**

For details about the error codes, see [Pasteboard Error Codes](../../../error-codes/pasteboard-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. |
| 12900003 | Another copy or paste operation is in progress. |
| 12900007 | Invalid destUri or file system error. |
| 12900008 | Failed to start progress. |
| 12900009 | Progress exits abnormally. |
| 12900010 | System error occurred during paste execution. |

**Example**

import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
@Entry
@Component
struct PasteboardTest {
 build() {
   RelativeContainer() {
     Column() {
       Column() {
         Button("Copy txt")
           .onClick(async ()=>{
              let text = "test";
              let pasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, text);
              let systemPasteboard = pasteboard.getSystemPasteboard();
              await systemPasteboard.setData(pasteData);
              let progressListenerInfo = (progress: pasteboard.ProgressInfo) => {
                console.info('progressListener success, progress:' + progress.progress);
              };
              let destPath: string = '/data/storage/el2/base/files/';
              let destUri : string = fileUri.getUriFromPath(destPath);
              let params: pasteboard.GetDataParams = {
                destUri: destUri,
                fileConflictOptions: pasteboard.FileConflictOptions.OVERWRITE,
                progressIndicator: pasteboard.ProgressIndicator.DEFAULT,
                progressListener: progressListenerInfo,
              };
              systemPasteboard.getDataWithProgress(params).then((pasteData: pasteboard.PasteData) => {
                console.info('getDataWithProgress success');
              }).catch((err: BusinessError) => {
                console.error('Failed to get PasteData. Cause: ' + err.message);
              })
          })
        }
      }
    }
  }
}

#### \[h2\]getChangeCount18+

getChangeCount(): number

Obtains the number of pasteboard content changes.

Returns the number of pasteboard content changes if this API is called successfully; returns **0** otherwise.

Even though the pasteboard data expires, or the data becomes empty because of the called [clearDataSync](#cleardatasync11) API, the number of data changes remains.

When the system is restarted, or the pasteboard service is restarted due to an exception, the number of pasteboard data changes counts from 0. In addition, copying the same data repeatedly is considered to change the data for multiple times. Therefore, each time the data is copied, the number of data changes increases.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Return value**

| Type | Description |
| :-- | :-- |
| number | The number of pasteboard content changes obtained. |

**Example**

import { BusinessError, pasteboard } from '@kit.BasicServicesKit';

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
try {
    let result : number = systemPasteboard.getChangeCount();
    console.info(\`Succeeded in getting the ChangeCount. Result: ${result}\`);
} catch (err) {
    console.error(\`Failed to get the ChangeCount. Cause: ${err.message}\`);
};

#### \[h2\]UpdateCallback 22+

type UpdateCallback = () => void

Callback to be invoked when the pasteboard content changes.

**System capability**: SystemCapability.MiscServices.Pasteboard

#### \[h2\]onRemoteUpdate(callback: UpdateCallback)22+

onRemoteUpdate(callback: UpdateCallback): void

Subscribes to the content change events of the pasteboard on a remote device. This callback is triggered when the pasteboard content on the remote device changes.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [UpdateCallback](#updatecallback-22) | Yes | Callback invoked when the pasteboard content changes. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.onRemoteUpdate(listener);

#### \[h2\]offRemoteUpdate(callback?: UpdateCallback)22+

offRemoteUpdate(callback?: UpdateCallback): void

Unsubscribes from the content change events of the pasteboard on a remote device.

**System capability**: SystemCapability.MiscServices.Pasteboard

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [UpdateCallback](#updatecallback-22) | No | Callback to be invoked when the pasteboard content on the remote device changes. If this parameter is not specified, remote listening will be disabled for all callbacks registered by the current application. |

**Example**

const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
let listener = () => {
    console.info('The remote pasteboard has changed.');
};
systemPasteboard.offRemoteUpdate(listener);
