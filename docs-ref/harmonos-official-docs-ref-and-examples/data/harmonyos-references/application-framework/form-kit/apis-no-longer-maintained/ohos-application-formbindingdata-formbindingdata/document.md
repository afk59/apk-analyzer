# @ohos.application.formBindingData (formBindingData)

The **FormBindingData** module provides APIs for widget data binding. You can use the APIs to create a **FormBindingData** object and obtain related information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/1ELN4utMSuq5TuPRGFk8dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE6F142DD12A2A8D717A5C204CC5C39BD595553184B0206BE72BFB3F6B697658)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This module is deprecated since API version 9. You are advised to use [formBindingData](../../arkts-apis/ohos-app-form-formbindingdata-formbindingdata/document.md) instead.

#### Modules to Import

import { formBindingData } from '@kit.FormKit';

#### FormBindingData

Describes a **FormBindingData** object.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | Object | No | No | Data to be displayed on the JS widget. The value can be an object containing multiple key-value pairs or a string in JSON format. |

#### formBindingData.createFormBindingData

createFormBindingData(obj?: Object | string): FormBindingData

Creates a **FormBindingData** object.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | Object|string | No | Data to be displayed on the JS widget. The value can be an object containing multiple key-value pairs or a string in JSON format. The image data is identified by **'formImages'**, and the content is multiple key-value pairs, each of which consists of an image identifier and image file descriptor. The final format is {'formImages': {'key1': fd1, 'key2': fd2}}. |

**Return value**

| Type | Description |
| :-- | :-- |
| [FormBindingData](#formbindingdata) | **FormBindingData** object created based on the passed data. |

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
      console.error(\`catch error, error: ${JSON.stringify(error)}\`);
    }
  }

  build() {
    Button('createFormBindingData')
      .onClick((event: ClickEvent) => {
        this.createFormBindingData();
      })
  }
}
