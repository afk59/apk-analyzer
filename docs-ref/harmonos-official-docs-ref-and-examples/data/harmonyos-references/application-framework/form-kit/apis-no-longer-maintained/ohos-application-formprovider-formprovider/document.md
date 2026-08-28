# @ohos.application.formProvider (formProvider)

The **FormProvider** module provides APIs related to the widget provider. You can use the APIs to update a widget, set the next refresh time for a widget, obtain widget information, and request a widget release.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/d31nKnRRSsKFa0kBYlD4kA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5160FA40E4BB65E056939131E9ACE8001A2B66CAC99F628061A6AF06BEF52FEB)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This module is deprecated since API version 9. You are advised to use [formProvider](../../arkts-apis/ohos-app-form-formprovider-formprovider/document.md) instead.

#### Modules to Import

import { formProvider } from '@kit.FormKit';

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void

Sets the next refresh time for a widget. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |
| minute | number | Yes | Time for the next refresh. The value must be greater than or equal to 5, in minutes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider } from '@kit.FormKit';
// Use an existing widget ID (formId).
let formId: string = '12400633174999288';
formProvider.setFormNextRefreshTime(formId, 5, (error: BusinessError) => {
  if (error.code) {
    console.error(\`formProvider setFormNextRefreshTime, errorCode: ${error.code}, errorMessage: ${error.message}\`);
  }
});

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number): Promise<void>

Sets the next refresh time for a widget. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |
| minute | number | Yes | Time for the next refresh. The value must be greater than or equal to 5, in minutes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider } from '@kit.FormKit';
// Use an existing widget ID (formId).
let formId: string = '12400633174999288';
formProvider.setFormNextRefreshTime(formId, 5).then(() => {
  console.info('formProvider setFormNextRefreshTime success');
}).catch((error: BusinessError) => {
  console.error(\`formProvider setFormNextRefreshTime, errorCode: ${error.code}, errorMessage: ${error.message}\`);
});

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void

Updates a widget. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget to update. |
| formBindingData | [formBindingData.FormBindingData](../ohos-application-formbindingdata-formbindingdata/document.md#formbindingdata) | Yes | Data to be used for the update. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider, formBindingData } from '@kit.FormKit';

// Use an existing widget ID (formId).
let formId: string = '12400633174999288';
let param: Record<string, string> = {
  'temperature': '22c',
  'time': '22:00'
}
let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, obj, (error: BusinessError) => {
  if (error.code) {
    console.error(\`formProvider updateForm, errorCode: ${error.code}, errorMessage: ${error.message}\`);
  }
});

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>

Updates a widget. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget to update. |
| formBindingData | [formBindingData.FormBindingData](../ohos-application-formbindingdata-formbindingdata/document.md#formbindingdata) | Yes | Data to be used for the update. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider, formBindingData } from '@kit.FormKit';

// Use an existing widget ID (formId).
let formId: string = '12400633174999288';
let param: Record<string, string> = {
  'temperature': '22c',
  'time': '22:00'
}
let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
formProvider.updateForm(formId, obj).then(() => {
  console.info('formProvider updateForm success');
}).catch((error: BusinessError) => {
  console.error(\`formProvider updateForm, errorCode: ${error.code}, errorMessage: ${error.message}\`);
});
