# Cross-Device Pasteboard Development

The cross-device pasteboard feature allows the system to automatically complete data transmission across devices. The following walks you through the development process.

#### Constraints

| 
**Device Version**

 | 

**Constraints**

 |
| :-- | :-- |
| 

HarmonyOS NEXT Developer Preview0 or later

 | 

-   The cross-device pasteboard feature must be enabled on both devices.
-   The same HUAWEI ID is logged on both devices.
-   Wi-Fi and Bluetooth must be enabled on both devices.
-   Both devices need to be unlocked and the screens need to be turned on during the process.

 |

#### Available APIs

Before developing a specific function, read [Reference Documents](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard) to obtain the detailed API description.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

getSystemPasteboard(): SystemPasteboard

 | 

Obtains a system pasteboard object.

 |
| 

createData(mimeType: string, value: ValueType): PasteData

 | 

Creates a pasteboard content object of the custom type.

 |
| 

setData(data: PasteData): Promise<void>

 | 

Writes data to the system pasteboard. This API uses a promise to return the result.

 |
| 

getData(callback: AsyncCallback<PasteData>): void

 | 

Obtains data from the system pasteboard. This API uses an asynchronous callback to return the result.

To use a customized component to access the pasteboard in the background, the application must have the **ohos.permission.READ\_PASTEBOARD** permission.

 |
| 

getRecordCount(): number

 | 

Obtains the number of data records in the pasteboard.

 |
| 

getPrimaryMimeType(): string

 | 

Obtains the data type of the first record in the pasteboard.

 |
| 

getPrimaryText(): string

 | 

Obtains the plain text of the first record.

 |

#### Development Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/uPg8rrdITdagM91eoFm6MQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AA6B79305A026BA9562AAC0023FB3C4048F64C7CCCB0EC160E490C094AAAF31)

Data copied for the across-device operation is valid within two minutes.

-   On device A, data is copied and written to the pasteboard service.
    
    import pasteboard from '@ohos.pasteboard';
    import { BusinessError } from '@ohos.base';
    
    export async function setPasteDataTest(): Promise<void> {
      let text: string = 'hello world';
      let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, text);
      let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
      await systemPasteBoard.setData(pasteData).catch((err: BusinessError) => {
        console.error(\`Failed to set pastedata. Code: ${err.code}, message: ${err.message}\`);
      });
    }
    

-   On device B, data is pasted and read from the pasteboard.
    
    import pasteboard from '@ohos.pasteboard';
    import { BusinessError } from '@ohos.base';
    
    export async function getPasteDataTest(): Promise<void> {
      let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
      systemPasteBoard.getData((err: BusinessError, data: pasteboard.PasteData) => {
        if (err) {
          console.error(\`Failed to get pastedata. Code: ${err.code}, message: ${err.message}\`);
          return;
        }
        // Process the data, such as obtaining the data type and number of records in the pasteboard.
        let recordCount: number = data.getRecordCount(); // Obtain the number of records in the pasteboard.
        let types: string = data.getPrimaryMimeType(); // Obtain the type of the data in the pasteboard.
        let primaryText: string = data.getPrimaryText(); // Obtain the content of the data in the pasteboard.
      });
    }
