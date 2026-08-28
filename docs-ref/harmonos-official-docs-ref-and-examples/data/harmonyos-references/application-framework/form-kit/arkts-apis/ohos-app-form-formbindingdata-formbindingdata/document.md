# @ohos.app.form.formBindingData (formBindingData)

The **FormBindingData** module provides APIs for widget data binding. You can use the APIs to create a **FormBindingData** object and obtain related information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/0iCALnErQ_qlljliRLRPug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA9804F63D7DCCE48F8F96EF55C7475A8D2F2BDD50D681AD094248E03A402247)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { formBindingData } from '@kit.FormKit';

#### ProxyData10+

Defines the subscription information about the widget update by proxy.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| key10+ | string | No | No | Subscriber ID of the widget update by proxy. The value is the same as that of the data publisher. |
| subscriberId10+ | string | No | Yes | Subscription condition of the widget update by proxy. The default value is the current widget ID (specified by **formId**). |

#### FormBindingData

Describes a **FormBindingData** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | Object | No | No | Data to be displayed on the widget. The value can be an object containing multiple key-value pairs or a string in JSON format. |
| proxies10+ | Array<[ProxyData](#proxydata10)\> | No | Yes | 
Subscription information of the widget update by proxy. The default value is an empty array.

**Model restriction**: This API can be used only in the stage model.

 |

#### formBindingData.createFormBindingData

createFormBindingData(obj?: Object | string): FormBindingData

Creates a **FormBindingData** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | Object | string | No | 
Data to be displayed on the widget. The value can be an object containing multiple key-value pairs or a string in JSON format. The image data is identified by **'formImages'**, and the content is multiple key-value pairs, each of which consists of an image identifier and image file descriptor. The final format is {'formImages': {'key1': fd1, 'key2': fd2}}.

**NOTE**

During [widget update](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-interaction-overview), when the widget UI receives widget data through @LocalStorageProp, the **FormBindingData** object is serialized, that is, the widget data is converted into the string type. Since API version 20, if the widget data is updated using shared memory, the total size of the updated data cannot exceed 10 MB, and the number of updated images cannot exceed 20. In API version 19 and earlier versions, the maximum number of image files is 5, and the maximum memory size of each image is 2 MB. Exceeding this 2 MB limit for any image will result in abnormal display.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [FormBindingData](#formbindingdata) | **FormBindingData** object created based on the passed data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**Example**

import { formBindingData } from '@kit.FormKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  content = this.getUIContext().getHostContext() as common.UIAbilityContext;
  pathDir: string = this.content.filesDir;

  createFormBindingData() {
    try {
      let filePath = this.pathDir + "/form.png";
      let file = fileIo.openSync(filePath);
      let formImagesParam: Record<string, number> = {
        'image': file.fd
      };
      let createFormBindingDataParam: Record<string, string | Record<string, number>> = {
        'name': '21°',
        'imgSrc': 'image',
        'formImages': formImagesParam
      };
      formBindingData.createFormBindingData(createFormBindingDataParam);
    } catch (error) {
      console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
    }
  }

  build() {
    Button('createFormBindingData')
      .onClick((event: ClickEvent) => {
        this.createFormBindingData();
      })
  }
}
