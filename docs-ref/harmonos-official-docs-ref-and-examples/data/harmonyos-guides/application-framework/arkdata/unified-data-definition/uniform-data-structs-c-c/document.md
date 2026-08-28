# Uniform Data Structs (C/C++)

#### When to Use

Uniform data structs are provided to define data of common [uniform data types](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-utd-h). For example, the data struct for the system-defined home screen icon (whose uniform data type is **OH\_UdsAppItem**) is provided to help you easily define the data.

Applications can directly use the uniform data structs in certain scenarios. For example, in the drag-and-drop operation across applications, you can write the data (encapsulated in a uniform struct) to be dragged to [DragEvent](../../../arkui/using-ndk-apis-to-build-uis/adding-interaction-events/drag-event/document.md). The target application (application requesting the data) reads the data from **DragEvent** and parses the data in the uniform data struct. Using uniform data structs for data interaction between applications effectively reduces the development workload in your application experience.

#### Basic Concepts

-   UDS
    
    A uniform data struct (UDS) defines the data of a certain type (specified by a UTD). Uniform data structs allow unified parsing standards to be used in data interaction, which minimizes the adaptation workload. Uniform data structs are used for data interaction across applications and devices, such as, the drag-and-drop operations.
    

#### Available APIs

For details about the APIs, see [uds.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-uds-h).

| API | Description |
| :-- | :-- |
| OH\_UdmfData\* OH\_UdmfData\_Create() | Creates an **OH\_UdmfData** instance and a pointer to it. |
| OH\_UdmfRecord\* OH\_UdmfRecord\_Create() | Creates an **OH\_UdmfRecord** instance and a pointer to it. |
| OH\_UdsPlainText\* OH\_UdsPlainText\_Create() | Creates an **OH\_UdsPlainText** instance and a pointer to it. |
| int OH\_UdmfRecord\_GetPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText) | Obtains **OH\_UdsPlainText** data from an **OH\_UdmfRecord** instance. |
| int OH\_UdsPlainText\_SetContent(OH\_UdsPlainText\* pThis, const char\* content) | Sets the plaintext content for an **OH\_UdsPlainText** instance. |
| int OH\_UdmfRecord\_AddPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText) | Adds **OH\_UdsPlainText** data to an **OH\_UdmfRecord** instance. |
| int OH\_UdmfData\_AddRecord(OH\_UdmfData\* pThis, OH\_UdmfRecord\* record) | Adds **OH\_UdmfRecord** data to an **OH\_UdmfData** instance. |
| OH\_UdsFileUri\* OH\_UdsFileUri\_Create() | Creates an **OH\_UdsFileUri** instance and a pointer to it. |
| int OH\_UdsFileUri\_SetFileUri(OH\_UdsFileUri\* pThis, const char\* fileUri) | Sets the URI information for an **OH\_UdsFileUri** instance. |
| int OH\_UdsFileUri\_SetFileType(OH\_UdsFileUri\* pThis, const char\* fileType) | Sets the file type for an **OH\_UdsFileUri** instance. |
| int OH\_UdmfRecord\_AddFileUri(OH\_UdmfRecord\* pThis, OH\_UdsFileUri\* fileUri) | Adds **OH\_UdsFileUri** data to an **OH\_UdmfData** instance. |
| int OH\_Udmf\_SetUnifiedData(Udmf\_Intention intention, OH\_UdmfData\* unifiedData,char\* key, unsigned int keyLen) | Sets an **OH\_UdmfData** instance in the UDMF database. |
| void OH\_UdsPlainText\_Destroy(OH\_UdsPlainText\* pThis) | Destroys an **OH\_UdsPlainText** instance. |
| void OH\_UdmfData\_Destroy(OH\_UdmfData\* pThis) | Destroys an **OH\_UdmfData** instance. |
| void OH\_UdsFileUri\_Destroy(OH\_UdsFileUri\* pThis) | Destroys an **OH\_UdsFileUri** instance. |

#### Adding Dynamic Link Libraries

Add the following libraries to **CMakeLists.txt**.

libudmf.so, libhilog\_ndk.z.so

#### Including Header Files

#include <database/udmf/uds.h>
#include <database/udmf/udmf.h>
#include <database/udmf/udmf\_meta.h>
#include <hilog/log.h>

#undef LOG\_TAG
#define LOG\_TAG "MY\_LOG"

#### Using the PlainText Data Struct

1.  Create a pointer to an **PlainText** object.
2.  Set content for the **PlainText** object.
3.  Obtain data.
4.  Destroy all the pointers created.

// 1. Create a pointer to an PlainText object.
OH\_UdmfRecord \*plainTextRecord = OH\_UdmfRecord\_Create();
OH\_UdsPlainText \*plainText = OH\_UdsPlainText\_Create();
char content\[\] = "hello world";

// 2. Set content for the PlainText object.
OH\_UdsPlainText\_SetContent(plainText, content);
OH\_UdmfRecord\_AddPlainText(plainTextRecord, plainText);

// 3. Obtain PlainText data.
OH\_UdsPlainText \*plainText2 = OH\_UdsPlainText\_Create();
OH\_UdmfRecord\_GetPlainText(plainTextRecord, plainText2);
const char \*content2 = OH\_UdsPlainText\_GetContent(plainText2);

OH\_LOG\_INFO(LOG\_APP, "content = %{public}s.", content2);
// 4. Destroy all the pointers created.
OH\_UdsPlainText\_Destroy(plainText);
OH\_UdmfRecord\_Destroy(plainTextRecord);
OH\_UdsPlainText\_Destroy(plainText2);

#### Using the fileUri Data Struct

1.  Create a struct for the **fileUri** data.
2.  Set the URL and description for the **fileUri**.
3.  Create an **OH\_UdmfRecord** object and set **fileUri** data to it.
4.  Obtain the **fileUri** data.
5.  Destroy all the pointers created.

// 1. Create a struct for the fileUri data.
const char \*uri = "https://xxx/xx/xx.jpg";
OH\_UdsFileUri \*fileUri = OH\_UdsFileUri\_Create();
// 2. Set the URL and description for the fileUri.
OH\_UdsFileUri\_SetFileUri(fileUri, uri);
OH\_UdsFileUri\_SetFileType(fileUri, UDMF\_META\_IMAGE);
// 3. Create an OH\_UdmfRecord object and set fileUri data to it.
OH\_UdmfRecord \*record = OH\_UdmfRecord\_Create();
OH\_UdmfRecord\_AddFileUri(record, fileUri);
// 4. Obtain the fileUri data.
OH\_UdsFileUri \*fileUri1 = OH\_UdsFileUri\_Create();
OH\_UdmfRecord\_GetFileUri(record, fileUri1);
const char \*fileUriStr = OH\_UdsFileUri\_GetFileUri(fileUri1);
OH\_LOG\_INFO(LOG\_APP, "fileUri1 = %{public}s.", fileUriStr);
// 5. Destroy all the pointers created.
OH\_UdsFileUri\_Destroy(fileUri);
OH\_UdmfRecord\_Destroy(record);
OH\_UdsFileUri\_Destroy(fileUri1);
