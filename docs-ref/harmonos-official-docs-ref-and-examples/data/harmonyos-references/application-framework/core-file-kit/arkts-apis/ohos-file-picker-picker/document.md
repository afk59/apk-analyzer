# @ohos.file.picker (Picker)

The **Picker** module encapsulates APIs such as **DocumentViewPicker**, **AudioViewPicker**, and **PhotoViewPicker** to provide capabilities of selecting and saving files of different types. An application can select the API as required. The APIs of this module must be called in UIAbility. Otherwise, the **FilePicker**, **AudioPicker**, or **PhotoPicker** cannot be started.

Chinese characters and non-digit characters in the URI are compiled into the corresponding ASCII code and concatenated to the URI returned by calling these APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/rg68Kwx8SRqzsyRlc5Ot5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7869A5FF5979419DD6C060B542C35B7F8D9A0D1F9DC35E907D18840C4379FC44)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import  { picker } from '@kit.CoreFileKit';

#### DocumentViewPicker

Provides APIs for selecting and saving documents in different formats. Before using the APIs of **DocumentViewPicker**, you need to create a **DocumentViewPicker** instance.

**System capability**: SystemCapability.FileManagement.UserFileService

#### \[h2\]constructor12+

constructor(context: Context)

A constructor used to create a **DocumentViewPicker** instance. This constructor is recommended. For details about how to obtain the context, see [getHostContext](../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#gethostcontext12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context (only **UIAbilityContext** is supported). For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |

**Example**

import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
            let documentPicker = new picker.DocumentViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]constructor12+

constructor()

A constructor used to create a **DocumentViewPicker** instance. This constructor is not recommended due to the potential risk of operation failure.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Example**

let documentPicker = new picker.DocumentViewPicker(); // Construction without parameter is not recommended. There is a possibility that the DocumentViewPicker instance fails to start.

#### \[h2\]constructor13+

constructor(context: Context, window: window.Window)

A constructor used to create a **DocumentViewPicker** object in a window created by an application. In other scenarios, you are advised to use **constructor(context: Context)** to create a **DocumentViewPicker** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/RVBhPVpuSOKx4831UNGYmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBE3D946BC089190475B30B52B0721C72FB7EEAF7CDFB53B57C6AF8AC9BCD287)

This method is supported on 2-in-1 devices and tablets since API version 19.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context (only **UIAbilityContext** is supported). For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| window | [window.Window](../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md) | Yes | Window instance created by the application. |

**Example**

import { common } from '@kit.AbilityKit';
import { picker } from '@kit.CoreFileKit';
import { window } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
            let windowClass: window.Window | undefined = undefined;
            windowClass = window.findWindow('test'); // Ensure that the window has been created. Here, 'test' is the value of the name parameter when the window is created.
            let documentPicker = new picker.DocumentViewPicker(context, windowClass);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]select

select(option?: DocumentSelectOptions): Promise<Array<string>>

Starts a **documentPicker** page for the user to select one or more documents. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [DocumentSelectOptions](#documentselectoptions) | No | Options for selecting documents. If this parameter is not specified, the **documentPicker** page is displayed by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | 
Promise used to return the URIs of the documents selected.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example07(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    }).catch((err: BusinessError) => {
      console.error(\`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}\`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]select

select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void

Starts a **documentPicker** page for the user to select one or more documents. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [DocumentSelectOptions](#documentselectoptions) | Yes | Options for selecting documents. |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the documents selected.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example08(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select(documentSelectOptions, (err: BusinessError, documentSelectResult: Array<string>) => {
      if (err) {
        console.error(\`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]select

select(callback: AsyncCallback<Array<string>>): void

Starts a **documentPicker** page for the user to select one or more documents. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the documents selected.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example09(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.select((err: BusinessError, documentSelectResult: Array<string>) => {
      if (err) {
        console.error(\`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' + JSON.stringify(documentSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]save

save(option?: DocumentSaveOptions): Promise<Array<string>>

Starts a **documentPicker** page for the user to save one or more documents. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [DocumentSaveOptions](#documentsaveoptions) | No | Options for saving the documents. If this parameter is not specified, a **documentPicker** page will be displayed for the user to enter the names of the documents to save. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | 
Promise used to return the URIs of the documents saved.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example10(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = \['DocumentViewPicker01.txt'\];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    }).catch((err: BusinessError) => {
      console.error(\`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}\`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]save

save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void

Starts a **documentPicker** page for the user to save one or more documents. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [DocumentSaveOptions](#documentsaveoptions) | Yes | Options for saving the documents. |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the documents saved.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example11(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = \['DocumentViewPicker02.txt'\];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions, (err: BusinessError, documentSaveResult: Array<string>) => {
      if (err) {
        console.error(\`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]save

save(callback: AsyncCallback<Array<string>>): void

Starts a **documentPicker** page for the user to save one or more documents. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the documents saved.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example12(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save((err: BusinessError, documentSaveResult: Array<string>) => {
      if (err) {
        console.error(\`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]getSelectedIndex14+

getSelectedIndex(): number

Obtains the index of the file suffix type of the file saved.

This method takes effect only when used with [save()](#save).

This method can be used only after [DocumentSaveOptions.fileSuffixChoices](#documentsaveoptions) is configured.

The index (number) returned by this method indicates the location of the file suffix specified in [DocumentSaveOptions.fileSuffixChoices](#documentsaveoptions). If no file suffix is specified, **getSelectedIndex()** returns **\-1**.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.FileManagement.UserFileService.FolderSelection

**Return value**

| Type | Description |
| :-- | :-- |
| number | Subscript (number) of the selected suffix type in [DocumentSaveOptions.fileSuffixChoices](#documentsaveoptions). The default value is **\-1**. |

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function exampleIndex(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let documentSaveOptions = new picker.DocumentSaveOptions();
    // Name of the file to save.
    documentSaveOptions.newFileNames = \['DocumentViewPicker01'\];
    // File suffix of the file to save.
    documentSaveOptions.fileSuffixChoices = \['txt', 'mp4', 'pdf'\];
    let documentPicker = new picker.DocumentViewPicker(context);
    documentPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
      if (documentSaveOptions.fileSuffixChoices != undefined && documentSaveResult != undefined) {
        // Obtain the index of the file suffix type of the file saved.
        let index = documentPicker.getSelectedIndex();
        // Obtain the file suffix type of the file saved.
        let selectedsuffix = documentSaveOptions.fileSuffixChoices\[index\];
        console.info ('DocumentViewPicker.save selectedsuffix is ' + selectedsuffix);
      }
      console.info('DocumentViewPicker.save successfully, documentSaveResult uri: ' + JSON.stringify(documentSaveResult));
    }).catch((err: BusinessError) => {
      console.error(\`DocumentViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}\`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`DocumentViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### AudioViewPicker

Provides APIs for selecting and saving audio clips. Before using the APIs of **AudioViewPicker**, you need to create an **AudioViewPicker** instance.

**System capability**: SystemCapability.FileManagement.UserFileService

#### \[h2\]constructor12+

constructor(context: Context)

A constructor used to create an **AudioViewPicker** instance. This constructor is recommended. For details about how to obtain the context, see [getHostContext](../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#gethostcontext12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context (only **UIAbilityContext** is supported). For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |

**Example**

import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
            let audioPicker = new picker.AudioViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]constructor12+

constructor()

A constructor used to create an **AudioViewPicker** instance. This constructor is not recommended due to the potential risk of operation failure.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Example**

let audioPicker = new picker.AudioViewPicker(); // Construction without parameter is not recommended. There is a possibility that the AudioViewPicker instance fails to start.

#### \[h2\]select

select(option?: AudioSelectOptions): Promise<Array<string>>

Starts an **audioPicker** page for the user to select one or more audio clips. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [AudioSelectOptions](#audioselectoptions) | No | Options for selecting audio clips. If this parameter is not specified, the **audioPicker** page is displayed by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | 
Promise used to return the URIs of the audio clips selected.

**Note**: For details about how to use the returned URIs, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example13(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let audioSelectOptions = new picker.AudioSelectOptions();
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    }).catch((err: BusinessError) => {
      console.error(\`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}\`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]select

select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void

Starts an **audioPicker** page for the user to select one or more audio clips. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [AudioSelectOptions](#audioselectoptions) | Yes | Options for selecting audio clips. |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the audio clips selected.

**Note**: For details about how to use the returned URIs, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example14(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let audioSelectOptions = new picker.AudioSelectOptions();
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select(audioSelectOptions, (err: BusinessError, audioSelectResult: Array<string>) => {
      if (err) {
        console.error(\`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]select

select(callback: AsyncCallback<Array<string>>): void

Starts an **audioPicker** page for the user to select one or more audio clips. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the audio clips selected.

**Note**: For details about how to use the returned URIs, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example15(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.select((err: BusinessError, audioSelectResult: Array<string>) => {
      if (err) {
        console.error(\`AudioViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('AudioViewPicker.select successfully, audioSelectResult uri: ' + JSON.stringify(audioSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]save

save(option?: AudioSaveOptions): Promise<Array<string>>

Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or more audio clips. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [AudioSaveOptions](#audiosaveoptions) | No | Options for saving audio clips. If this parameter is not specified, an **audioPicker** page will be displayed for the user to enter the names of the files to save. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | 
Promise used to return the URIs of the audio clips saved.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example16(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let audioSaveOptions = new picker.AudioSaveOptions();
    audioSaveOptions.newFileNames = \['AudioViewPicker01.mp3'\];
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions).then((audioSaveResult: Array<string>) => {
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult))
    }).catch((err: BusinessError) => {
      console.error(\`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}\`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]save

save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void

Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or more audio clips. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [AudioSaveOptions](#audiosaveoptions) | Yes | Options for saving audio clips. |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the audio clips saved.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example17(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let audioSaveOptions = new picker.AudioSaveOptions();
    audioSaveOptions.newFileNames = \['AudioViewPicker02.mp3'\];
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save(audioSaveOptions, (err: BusinessError, audioSaveResult: Array<string>) => {
      if (err) {
        console.error(\`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### \[h2\]save

save(callback: AsyncCallback<Array<string>>): void

Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or more audio clips. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the audio clips saved.

**Note**: For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example18(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let audioPicker = new picker.AudioViewPicker(context);
    audioPicker.save((err: BusinessError, audioSaveResult: Array<string>) => {
      if (err) {
        console.error(\`AudioViewPicker.save failed with err, code is: ${err.code}, message is: ${err.message}\`);
        return;
      }
      console.info('AudioViewPicker.save successfully, audioSaveResult uri: ' + JSON.stringify(audioSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
        console.error(\`AudioViewPicker failed with err, code is: ${err.code}, message is: ${err.message}\`);
  }
}

#### DocumentSelectMode11+

Enumerates the types of documents selected.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService.FolderSelection

| Name | Value | Description |
| :-- | :-- | :-- |
| FILE | 0 | File (default). |
| FOLDER | 1 | Folder. |
| MIXED | 2 | Mixed type of files and folders. |

#### DocumentSelectOptions

Defines the options for selecting documents.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| maxSelectNumber10+ | number | No | Yes | 
Maximum number of files that can be selected.

In API version 20 and earlier versions, a maximum of 500 files can be selected at a time. The default value is 500. Directories can be selected only on devices that have the system capability. A maximum of one directory can be selected.

The restriction is canceled in API version 21 and later. Due to system capability restrictions, if too many files are selected at a time, the functionality may be abnormal or the processing performance may be poor. It is recommended that a maximum of 10,000 files be selected at a time.

**System capability**: SystemCapability.FileManagement.UserFileService

 |
| defaultFilePathUri10+ | string | No | Yes | URI of the file or directory that can be selected. It is empty by default (the recently opened page is displayed). |
| fileSuffixFilters10+ | Array<string> | No | Yes | 

Suffix of the document to select.

The value is a string array. Each element specifies an option, which includes at most two parts with a vertical bar (|) in between. The first part is the description, and the second part is the document suffix. If there is no "|", the option does not have the description. Each filter suffix can contain multiple suffixes, separated by a comma (,). The length of the input array cannot exceed 100 characters, for example, \['Images (.png, .jpg)|.png,.jpg', 'Documents|.txt', 'Videos|.mp4', '.pdf'\].

By default, no filtering is performed, that is, all documents are selected. The wildcard \['All files (\*.\*)|.\*'\] can be used on 2-in-1 devices to display all files. (Mobile phones can support this configuration since API version 17.)

This parameter is available only to the devices that have the required system capability. **System capability**: SystemCapability.FileManagement.UserFileService

 |
| selectMode11+ | [DocumentSelectMode](#documentselectmode11) | No | Yes | 

Type of the document selected by Picker. The default value is **FILE** (file type).

**System capability**: SystemCapability.FileManagement.UserFileService.FolderSelection

 |
| authMode12+ | boolean | No | Yes | 

Whether to start Picker.

Default value: **false**. If **authMode** is **true**, **defaultFilePathUri** is mandatory, which specifies the URI of the file allowed to access.

**Device behavior differences**: This parameter can be used on 2-in-1 devices but has no effect on other devices.

**System capability**: SystemCapability.FileManagement.UserFileService.FolderSelection

 |
| multiAuthMode15+ | boolean | No | Yes | 

Whether to enable the batch authorization mode.

The value **false** (default) means to disable the batch authorization mode; the value **true** means to enable the batch authorization mode. The **multiUriArray** parameter only takes effect when **multiAuthMode** is set to **true**.

**Device behavior differences**: This parameter can be used on smartphones but has no effect on other devices.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| multiUriArray15+ | Array<string> | No | Yes | 

Whether to pass the URIs for batch authorization (only files are supported). This parameter is used together with **multiAuthMode** and does not take effect when **multiAuthMode** is set to **false**. By default, this parameter is left empty. (The files displayed on the batch authorization page are empty.)

**Device behavior differences**: This parameter can be used on smartphones but has no effect on other devices.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| mergeMode15+ | [MergeTypeMode](#mergetypemode15) | No | Yes | 

Whether to enable the aggregation view mode for a file management application. The default value is **DEFAULT**, indicating that this parameter does not take effect and the aggregation view is disabled. If this parameter is set to a value other than **DEFAULT**, other parameters do not take effect.

**Device behavior differences**: This parameter can be used on smartphones but has no effect on other devices.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| isEncryptionSupported19+ | boolean | No | Yes | 

Whether to support encryption (only files are supported). The default value is **false**. If this parameter is set to **true**, files can be encrypted on the Picker page.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.FileManagement.UserFileService

 |

#### DocumentPickerMode12+

Enumerates the modes for saving documents.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Standard mode. |
| DOWNLOAD | 1 | 
Download mode.

**Note**: The directories created in DOWNLOAD mode are used only to save files. There is no access isolation between directories. You are advised not to save sensitive application data.

 |

#### MergeTypeMode15+

Enumerates file aggregation types.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.FileManagement.UserFileService

**Device behavior differences**: This API can be called on mobile phones but has no effect on other devices.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Default mode, indicating that this parameter does not take effect. |
| AUDIO | 1 | Audio mode. |
| VIDEO | 2 | Video mode. |
| DOCUMENT | 3 | Document mode. |
| PICTURE | 4 | Image mode. |

#### DocumentSaveOptions

Defines the options for saving documents.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| newFileNames | Array<string> | No | Yes | Name of the document to save. If this parameter is not specified, the user needs to enter the file name. |
| defaultFilePathUri10+ | string | No | Yes | URI of the file or directory to save. This parameter is left empty by default. |
| fileSuffixChoices10+ | Array<string> | No | Yes | 
Document suffix of the document to save.

The value is a string array. Each element specifies an option, which includes at most two parts with a vertical bar (|) in between. The first part is the description, and the second part is the document suffix. If there is no "|", the option does not have the description. By default, all documents are saved.

 |
| pickerMode12+ | [DocumentPickerMode](#documentpickermode12) | No | Yes | 

Mode for starting Picker.

Default value: **DEFAULT**. If **pickerMode** is **DOWNLOAD**, the settings of **newFileNames**, **defaultFilePathUri**, and **fileSuffixChoices** do not take effect.

 |

#### AudioSelectOptions

Defines the options for selecting audio clips.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| maxSelectNumber12+ | number | No | Yes | 
Maximum number of audio clips that can be selected.

Default value: **1**

Value range: 1 to 500

 |

#### AudioSaveOptions

Defines the options for saving audio clips.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| newFileNames | Array<string> | No | Yes | File name of the audio clip to save. If this parameter is not specified, the user needs to enter the file name. |

#### PhotoViewPicker(deprecated)

Provides APIs for selecting and saving images or videos. You are advised to use [PhotoViewPicker of PhotoAccessHelper](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/class-photoviewpicker/document.md) to select a file. Before using the APIs of **PhotoViewPicker**, you need to create a **PhotoViewPicker** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/cMlkpOKZQjqYeGVdobmmnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DDEDC4429750ABD9A598D87DA05B756C7D9BF8D699EE14B62C78C5EB4B7B40B)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [photoAccessHelper.PhotoViewPicker](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/class-photoviewpicker/document.md) instead.

**System capability**: SystemCapability.FileManagement.UserFileService

#### \[h2\]constructor(deprecated)

constructor(context: Context)

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context (only **UIAbilityContext** is supported). For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |

A constructor used to create a **PhotoViewPicker** instance. This constructor is recommended. For details about how to obtain the context, see [getHostContext](../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#gethostcontext12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/ZDaXWF7KQKGbRCQ8usit9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2740C8C55F754CBFB68D77AA7891218334BA5B2684461460F153AF0BD9F15B85)

This API is supported since API version 12 and deprecated since API version 18. You are advised to use [photoAccessHelper.PhotoViewPicker](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/class-photoviewpicker/document.md) instead.

**Example**

import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // Ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
            let photoPicker = new picker.PhotoViewPicker(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]constructor(deprecated)

constructor()

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.UserFileService

A constructor used to create a **PhotoViewPicker** instance. This constructor is not recommended due to the potential risk of operation failure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/2jv1XdOsTeeLJs9Sp9RuZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15A5330E678E1AA9E24E0DE9781F7B492D9414978E591FC5D70E4DAAD1664258)

This API is supported since API version 12 and deprecated since API version 18. You are advised to use [photoAccessHelper.PhotoViewPicker](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/class-photoviewpicker/document.md) instead.

**Example**

let photoPicker = new picker.PhotoViewPicker(); // Construction without parameter is not recommended. There is a possibility that the PhotoViewPicker instance fails to start.

#### \[h2\]select(deprecated)

select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses a promise to return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to select.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/_A5zfbtcS2ipKYGYKRV5xQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84017FB9897A3CF26364255C8E1952C6F20875BC8D4E6243928F8A085D2D86DC)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [photoAccessHelper.PhotoViewPicker#select](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/class-photoviewpicker/document.md#select) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [PhotoSelectOptions](#photoselectoptionsdeprecated) | No | Options for selecting images or videos. If this parameter is not specified, images and videos are selected by default. A maximum of 50 files can be selected. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PhotoSelectResult](#photoselectresultdeprecated)\> | 
Promise used to return the URIs of the images or videos selected.

**Note**: The **photoUris** in the **PhotoSelectResult** object returned by this API can be used only by [photoAccessHelper.getAssets](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoaccesshelper/document.md#getassets). For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example01(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE\_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions).then((photoSelectResult: picker.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    }).catch((err: BusinessError) => {
      console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}

#### \[h2\]select(deprecated)

select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to select.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/e7cyi206TaKNqgApeA1Aww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD50CE6D33A06D7A16456E3D2BC4DCD817F5E9640066D4D19BE373E0B60C136B)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [photoAccessHelper.PhotoViewPicker#select](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/class-photoviewpicker/document.md#select-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [PhotoSelectOptions](#photoselectoptionsdeprecated) | Yes | Options for selecting images or videos. |
| callback | AsyncCallback<[PhotoSelectResult](#photoselectresultdeprecated)\> | Yes | 
Callback used to return the images or videos selected.

**Note**: The **photoUris** in the **PhotoSelectResult** object returned by this API can be used only by [photoAccessHelper.getAssets](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoaccesshelper/document.md#getassets). For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example02(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSelectOptions = new picker.PhotoSelectOptions();
    photoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE\_TYPE;
    photoSelectOptions.maxSelectNumber = 5;
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select(photoSelectOptions, (err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}

#### \[h2\]select(deprecated)

select(callback: AsyncCallback<PhotoSelectResult>): void

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/rwRkxiGYR5i8sed7QGSxIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE8FBC16965867B7E8ECB2ED46E13A391F3D87261C19517BAD94E7909FC2D0A5)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [photoAccessHelper.PhotoViewPicker#select](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/class-photoviewpicker/document.md#select-2) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PhotoSelectResult](#photoselectresultdeprecated)\> | Yes | 
Callback used to return the images or videos selected.

**Note**: The **photoUris** in the **PhotoSelectResult** object returned by this API can be used only by [photoAccessHelper.getAssets](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoaccesshelper/document.md#getassets). For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example03(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.select((err: BusinessError, photoSelectResult: picker.PhotoSelectResult) => {
      if (err) {
        console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.select successfully, photoSelectResult uri: ' + JSON.stringify(photoSelectResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}

#### \[h2\]save(deprecated)

save(option?: PhotoSaveOptions): Promise<Array<string>>

Starts a **photoPicker** page for the user to save one or more images or videos. This API uses a promise to return the result. You can pass in **PhotoSaveOptions** to specify the URIs of the images or videos to save.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/vv6FGeaARdGceSlJ407nZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBEB3FDDF265E163AB6E7C53B8D19610C1D185FBC1EEBAD83675FCF2F0A364B3)

This API is supported since API version 9 and deprecated since API version 12. Use [SaveButton](../../../arkui/arkts-components/security/savebutton/document.md) instead.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [PhotoSaveOptions](#photosaveoptionsdeprecated) | No | Options for saving images or videos. If this parameter is not specified, a **photoPicker** page will be displayed for the user to enter the names of the files to save. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | 
Promise used to return the URIs of the images or videos saved.

**Note**: This API saves files in **Files**, not in **Gallery**. For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example04(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = \['PhotoViewPicker01.jpg', 'PhotoViewPicker01.mp4'\];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions).then((photoSaveResult: Array<string>) => {
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    }).catch((err: BusinessError) => {
      console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
      console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}

#### \[h2\]save(deprecated)

save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void

Starts a **photoPicker** page for the user to save one or more images or videos. This API uses an asynchronous callback to return the result. You can pass in **PhotoSaveOptions** to specify the URIs of the images or videos to save.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/CcxGm8FcQ_mkdqPVn4yB7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4153ECD0B84FFB04EBD34B761A77407C795B8F4DC2AC895C0838738D1417A458)

This API is supported since API version 9 and deprecated since API version 12. Use [SaveButton](../../../arkui/arkts-components/security/savebutton/document.md) instead.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | [PhotoSaveOptions](#photosaveoptionsdeprecated) | Yes | Options for saving images or videos. |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the images or videos saved.

**Note**: This API saves files in **Files**, not in **Gallery**. For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example05(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoSaveOptions = new picker.PhotoSaveOptions();
    photoSaveOptions.newFileNames = \['PhotoViewPicker02.jpg','PhotoViewPicker02.mp4'\];
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save(photoSaveOptions, (err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}

#### \[h2\]save(deprecated)

save(callback: AsyncCallback<Array<string>>): void

Starts a **photoPicker** page for the user to save one or more images or videos. This API uses an asynchronous callback to return the URIs of the images or videos to save.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/FL1NxK5TQ4Ga2TG_NSczyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32F976224101FAE616DCD404265837DD63517E073839EE32C242BF70D10D13CE)

This API is supported since API version 9 and deprecated since API version 12. Use [SaveButton](../../../arkui/arkts-components/security/savebutton/document.md) instead.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | 
Callback invoked to return the URIs of the images or videos saved.

**Note**: This API saves files in **Files**, not in **Gallery**. For details about how to use the returned URIs, see [Using a Document URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-document-uri).

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import  { picker } from '@kit.CoreFileKit';
async function example06(context: common.UIAbilityContext) { // Ensure that context is converted from UIAbilityContext.
  try {
    let photoPicker = new picker.PhotoViewPicker(context);
    photoPicker.save((err: BusinessError, photoSaveResult: Array<string>) => {
      if (err) {
        console.error('PhotoViewPicker.save failed with err: ' + JSON.stringify(err));
        return;
      }
      console.info('PhotoViewPicker.save successfully, photoSaveResult uri: ' + JSON.stringify(photoSaveResult));
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
  }
}

#### PhotoViewMIMETypes(deprecated)

Enumerates the media file types that can be selected.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/dtMlGXXjQ8q6RAApl2R4tg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F603C28805DA9149085F55980617FC65AA1AD876CA90CA5A27F82A378202988)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [photoAccessHelper.PhotoViewMIMETypes](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#photoviewmimetypes) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Value | Description |
| :-- | :-- | :-- |
| IMAGE\_TYPE | 'image/\*' | 
Image.

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |
| VIDEO\_TYPE | 'video/\*' | 

Video.

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |
| IMAGE\_VIDEO\_TYPE | '\*/\*' | 

Image and video.

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |

#### PhotoSelectOptions(deprecated)

Defines the options for selecting images or videos.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ETfrV29ZSEqq6eYFMg8bFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10FB413B816418BC23F944F4B30D777F9AFCC5025EE800D33BB093AA9447D9A2)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [photoAccessHelper.PhotoSelectOptions](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/classes-others/document.md#photoselectoptions) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| MIMEType | [PhotoViewMIMETypes](#photoviewmimetypesdeprecated) | No | Yes | 
Media file types to select. If this parameter is not specified, **IMAGE\_VIDEO\_TYPE** is used by default.

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |
| maxSelectNumber | number | No | Yes | 

Maximum number of media files that can be selected. The default value is **50**, and the maximum value is **500**.

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |

#### PhotoSelectResult(deprecated)

Defines information about the images or videos selected.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/RBl_Rn8JQfqIdU7q7vN6Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8993A2833D63F6042C9E43C1978C307153694F2B28FE3C2A3284267DDBC25F4)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [photoAccessHelper.PhotoSelectResult](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/classes-others/document.md#photoselectresult) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| photoUris | Array<string> | No | No | 
URIs of the media files selected. This URI array can be used only by [photoAccessHelper.getAssets](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interface-photoaccesshelper/document.md#getassets). For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |
| isOriginalPhoto | boolean | No | No | 

Whether the selected image is the original one. The value **true** means the selected image is the original one; the value **false** means the opposite.

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |

#### PhotoSaveOptions(deprecated)

Defines the options for saving images or videos.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/y6p5pTlgRy-JLXHlkXDAvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEF8C2C31F2EAFFBB54645C11E08E7898B60B46C5195B8F5B85E3ABE6AF6BC03)

This API is supported since API version 9 and deprecated since API version 12. Use [SaveButtonOptions](../../../arkui/arkts-components/security/savebutton/document.md#savebuttonoptions) instead.

**System capability**: SystemCapability.FileManagement.UserFileService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| newFileNames | Array<string> | No | Yes | 
File name of the image or video to save. If this parameter is not specified, the user needs to enter the file name.

**Note**: This API is supported since API version 9 and deprecated since API version 18.

 |
