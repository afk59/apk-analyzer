# @ohos.app.form.formProvider (formProvider)

The **formProvider** module provides APIs to obtain widget information, update widgets, and set the update time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/RlMSgatZSXClBCmU98-8_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20244A8CAC43CCC6E34B2A5707339D3C499FB05A8A91F8919F3172A49CC67A91)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { formProvider } from '@kit.FormKit';

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void

Sets the next refresh time for a widget. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |
| minute | number | Yes | Time after which a widget is updated. The value is greater than or equal to 5, in minutes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501002 | The number of forms exceeds the maximum allowed. |
| 16501003 | The form cannot be operated by the current application. |

**Example**

import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';
try {
  formProvider.setFormNextRefreshTime(formId, 5, (error: BusinessError) => {
    if (error) {
      console.error(\`callback error, code: ${error.code}, message: ${error.message})\`);
      return;
    }
    console.info(\`formProvider setFormNextRefreshTime success\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.setFormNextRefreshTime

setFormNextRefreshTime(formId: string, minute: number): Promise<void>

Sets the next refresh time for a widget. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |
| minute | number | Yes | Time after which a widget is updated. The value is greater than or equal to 5, in minutes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501002 | The number of forms exceeds the maximum allowed. |
| 16501003 | The form cannot be operated by the current application. |

**Example**

import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';
try {
  formProvider.setFormNextRefreshTime(formId, 5).then(() => {
    console.info(\`formProvider setFormNextRefreshTime success\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void

Updates a widget. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/QDec5m3oRJqfedu31-6pmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2305A5480F04A0D083B510763A1C64446BC55DA04DB6E6F09192925F3E688484)

Starting from API version 20, when widget refresh data is updated via shared memory, the total size of the refreshed data must not exceed 10 MB, and the number of refreshed images must not exceed 20. For API version 19 and earlier versions, the maximum number of image files is 5, with a 2 MB memory limit per image. Any images that exceed these limits will display abnormally.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget to update. |
| formBindingData | [formBindingData.FormBindingData](../ohos-app-form-formbindingdata-formbindingdata/document.md#formbindingdata) | Yes | Data to be used for the update. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**Example**

import { formBindingData, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';
try {
  let param: Record<string, string> = {
    'temperature': '22c',
    'time': '22:00'
  }
  let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
  formProvider.updateForm(formId, obj, (error: BusinessError) => {
    if (error) {
      console.error(\`callback error, code: ${error.code}, message: ${error.message})\`);
      return;
    }
    console.info(\`formProvider updateForm success\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.updateForm

updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>

Updates a widget. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/sb5udev3SVOEMMTl9T4LTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE420DF82EA4684F7F44BDDF059E4E2E9948394EFE0A6628EDA16E2C2EDD351A)

Starting from API version 20, when widget refresh data is updated via shared memory, the total size of the refreshed data must not exceed 10 MB, and the number of refreshed images must not exceed 20. For API version 19 and earlier versions, the maximum number of image files is 5, with a 2 MB memory limit per image. Any images that exceed these limits will display abnormally.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget to update. |
| formBindingData | [formBindingData.FormBindingData](../ohos-app-form-formbindingdata-formbindingdata/document.md#formbindingdata) | Yes | Data to be used for the update. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**Example**

import { formBindingData, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';
let param: Record<string, string> = {
  'temperature': '22c',
  'time': '22:00'
}
let obj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
try {
  formProvider.updateForm(formId, obj).then(() => {
    console.info(\`formProvider updateForm success\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.getFormsInfo

getFormsInfo(callback: AsyncCallback<Array<formInfo.FormInfo>>): void

Obtains the application's widget information on the device. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[formInfo.FormInfo](../ohos-app-form-forminfo-forminfo/document.md)\>> | Yes | Callback used to return the information obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**Example**

import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formProvider.getFormsInfo((error, data) => {
    if (error) {
      console.error(\`callback error, code: ${error.code}, message: ${error.message})\`);
      return;
    }
    console.info(\`formProvider getFormsInfo, data: ${JSON.stringify(data)}\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.getFormsInfo

getFormsInfo(filter: formInfo.FormInfoFilter, callback: AsyncCallback<Array<formInfo.FormInfo>>): void

Obtains the application's widget information that meets a filter criterion on the device. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [formInfo.FormInfoFilter](../ohos-app-form-forminfo-forminfo/document.md#forminfofilter) | Yes | Filter criterion. |
| callback | AsyncCallback<Array<[formInfo.FormInfo](../ohos-app-form-forminfo-forminfo/document.md)\>> | Yes | Callback used to return the information obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

const filter: formInfo.FormInfoFilter = {
  // get info of forms belong to module entry.
  moduleName: 'entry'
};
try {
  formProvider.getFormsInfo(filter, (error, data) => {
    if (error) {
      console.error(\`callback error, code: ${error.code}, message: ${error.message})\`);
      return;
    }
    console.info(\`formProvider getFormsInfo, data: ${JSON.stringify(data)}\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.getFormsInfo

getFormsInfo(filter?: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>

Obtains information about widgets that meet the criteria of the current application. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [formInfo.FormInfoFilter](../ohos-app-form-forminfo-forminfo/document.md#forminfofilter) | No | Filter criterion. By default, no value is passed, indicating that no filtering is performed. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[formInfo.FormInfo](../ohos-app-form-forminfo-forminfo/document.md)\>> | Promise used to return the information obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

const filter: formInfo.FormInfoFilter = {
  // get info of forms belong to module entry.
  moduleName: 'entry'
};
try {
  formProvider.getFormsInfo(filter).then((data: formInfo.FormInfo\[\]) => {
    console.info(\`formProvider getFormsInfo, data: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.openFormEditAbility18+

openFormEditAbility(abilityName: string, formId: string, isMainPage?: boolean): void

Opens the widget editing page.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityName | string | Yes | Ability name on the editing page. |
| formId | string | Yes | Widget ID. |
| isMainPage | boolean | No | 
Whether the page is the main editing page.

\- **true**: The page is the main editing page.

\- **false**: The page is not the main editing page.

Default value: **true**.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.function openFormEditAbility can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501003 | The form cannot be operated by the current application. |
| 16501007 | Form is not trust. |

**Example**

import { formProvider } from '@kit.FormKit';

const TAG: string = 'FormEditDemo-Page\] -->';

@Entry
@Component
struct Page {
  @State message: string = 'Hello World';

  aboutToAppear(): void {
    console.info(\`${TAG} aboutToAppear.....\`);
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('PageHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Top },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          console.info(\`${TAG} onClick.....\`);
          formProvider.openFormEditAbility('ability://EntryFormEditAbility', '1386529921');
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### formProvider.openFormManager18+

openFormManager(want: Want): void

Opens the Widget Manager page of the current application.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | 
Parameter that must contain the following fields:

**bundleName**: bundle name of widget.

**abilityName**: ability name of the widget.

**parameters**:

\- **ohos.extra.param.key.form\_dimension**: [Widget dimension](../ohos-app-form-forminfo-forminfo/document.md#formdimension).

\- **ohos.extra.param.key.form\_name**: Widget name.

\- **ohos.extra.param.key.module\_name**: module name of the widget.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/sQyLuoWiQ1qWIrgq4UY8ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF0E6E9ABDCC57825233155C3470C861BD6DA5238F2E25651356C1DF5DB6E026)

If the parameter is not set or the specified widget does not exist, the default widget configured in [form\_config.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration#widget-configuration) is displayed by default.

**Error codes**

For details about the error codes, see [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**Example**

import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

const want: Want = {
  bundleName: 'com.example.formbutton',
  abilityName: 'EntryFormAbility',
  parameters: {
    'ohos.extra.param.key.form\_dimension': 2,
    'ohos.extra.param.key.form\_name': 'widget',
    'ohos.extra.param.key.module\_name': 'entry'
  },
};
try {
  formProvider.openFormManager(want);
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.getPublishedFormInfoById(deprecated)

getPublishedFormInfoById(formId: string): Promise<formInfo.FormInfo>

Obtains the information of the widget that has been added to the home screen on the device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ChIOsCMRTQyMDCOqlazdbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4A4822948CD8D3602579580B9089E95C6BD110C1164451CC3B41049DF237A66)

This field is supported since API version 18 and deprecated since API version 20. You are advised to use [getPublishedRunningFormInfoById](#formprovidergetpublishedrunningforminfobyid20) instead.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[formInfo.FormInfo](../ohos-app-form-forminfo-forminfo/document.md#forminfo)\> | Promise used to return the information obtained. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

const formId: string = '388344236';
try {
  formProvider.getPublishedFormInfoById(formId).then((data: formInfo.FormInfo) => {
    console.info(\`formProvider getPublishedFormInfoById, data: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.getPublishedFormInfos(deprecated)

getPublishedFormInfos(): Promise<Array<formInfo.FormInfo>>

Obtains the information of all widgets that have been added to the home screen on the device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/wkLpo1n3Rn-sbg1BSb4t5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE03B0FCB140E78C84B7AF7B4F0142F0CC1037C9F4CDF02FFAAE3BE86B2C358E)

This field is supported since API version 18 and deprecated since API version 20. You are advised to use [getPublishedRunningFormInfos](#formprovidergetpublishedrunningforminfos20) instead.

**System capability**: SystemCapability.Ability.Form

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[formInfo.FormInfo](../ohos-app-form-forminfo-forminfo/document.md)\>> | Promise used to return the information obtained. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formProvider.getPublishedFormInfos().then((data: formInfo.FormInfo\[\]) => {
    console.info(\`formProvider getPublishedFormInfos, data: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.requestOverflow20+

requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>

Requests an animation. This API takes effect only for [scene-based widgets](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration#sceneanimationparams-field). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ImasXmU8QTecqDyR0K9Hwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B25B76FCDCF0A4B7CD9D22F8F895AF2FAC251ADC54FF858F73FDA5DCEDA5A05)

1.  This API is unavailable in power saving mode. Otherwise, error code 16501000 will be reported.
2.  When the device's thermal level reaches HOT and no tap event occurs, this API reports error code 16501000. When the thermal level reaches OVERHEATED, this API reports error code 16501000 in all cases. For details, see [ThermalLevel](../../../../system/basic-functions/basic-services-kit/arkts-apis/device-management/ohos-thermal-thermal-management/document.md#thermallevel).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |
| overflowInfo | [formInfo.OverflowInfo](../ohos-app-form-forminfo-forminfo/document.md#overflowinfo20) | Yes | Animation request parameter information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.function requestOverflow can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |
| 16501011 | The form can not support this operation. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';
let overflowInfo: formInfo.OverflowInfo = {
  area: {
    left: -10,
    top: -10,
    width: 180,
    height: 180
  },
  duration: 1000,
  useDefaultAnimation: false,
};

try {
  formProvider.requestOverflow(formId, overflowInfo).then(() => {
    console.info('requestOverflow succeed.');
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.cancelOverflow20+

cancelOverflow(formId: string): Promise<void>

Cancels an animation. This API takes effect only for [scene-based widgets](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration#sceneanimationparams-field). This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.function cancelOverflow can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |
| 16501011 | The form can not support this operation. |

**Example**

import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';

try {
  formProvider.cancelOverflow(formId).then(() => {
    console.info('cancelOverflow succeed.');
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.getFormRect20+

getFormRect(formId: string): Promise<formInfo.Rect>

Obtains the position and dimension of a widget. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[formInfo.Rect](../ohos-app-form-forminfo-forminfo/document.md#rect20)\> | Promise used to return the position and dimension of the widget relative to the upper-left corner of the screen, in vp. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported.function getFormRect can not work correctly due to limited device capabilities. |
| 16500050 | IPC connection error. |
| 16500060 | Service connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288';

try {
  formProvider.getFormRect(formId).then((data: formInfo.Rect) => {
    console.info(\`getFormRect succeed, data: ${JSON.stringify(data)}\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.getPublishedRunningFormInfoById20+

getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>

Obtains the information of a specified widget that has been added to the home screen. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[formInfo.RunningFormInfo](../ohos-app-form-forminfo-forminfo/document.md#runningforminfo20)\> | Promise used to return the information about the widgets that meet the requirements, including the widget name and dimension. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501003 | The form cannot be operated by the current application. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

const formId: string = '388344236';

try {
  formProvider.getPublishedRunningFormInfoById(formId).then((data: formInfo.RunningFormInfo) => {
    console.info(\`formProvider getPublishedRunningFormInfoById, data: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}\`);
}

#### formProvider.getPublishedRunningFormInfos20+

getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>

Obtains information about all widgets that have been added to the home screen. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[formInfo.RunningFormInfo](../ohos-app-form-forminfo-forminfo/document.md#runningforminfo20)\>> | Promise used to return the information about widgets that meet the requirements. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |

**Example**

import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formProvider.getPublishedRunningFormInfos().then((data: formInfo.RunningFormInfo\[\]) => {
    console.info(\`formProvider getPublishedRunningFormInfos, data: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.reloadForms22+

reloadForms(context: UIAbilityContext, moduleName: string, abilityName: string, formName: string): Promise<number>

Reloads widgets. For widgets with the same **moduleName**, **abilityName**, and **formName** of the current application, each widget has a different widget ID after being added to the home screen for multiple times. Widget providers can use this API to batch update widgets that have different IDs but share the same **moduleName**, **abilityName**, and **formName**. Invoked in the main process of the application, this API notifies the FormExtension process to perform batch updates. It can only be called within a [UIAbility](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) and uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | [UIAbility](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context, which is used for verification. |
| moduleName | string | Yes | Module name of the widget. |
| abilityName | string | Yes | Ability name of the widget. |
| formName | string | Yes | Name of the widget configured in [form\_config.json](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-ui-widget-configuration#fields-in-configuration-file). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of widgets requested for update. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 16501000 | An internal functional error occurred. |

**Example**

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider } from '@kit.FormKit';

try {
  // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
  let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // Replace the information with the actual widget information to be updated.
  let moduleName: string = 'entry';
  let abilityName: string = 'EntryFormAbility';
  let formName: string = 'formName';
  formProvider.reloadForms(context, moduleName, abilityName, formName).then((reloadNum: number) => {
    console.info(\`reloadForms success, reload number: ${reloadNum}\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}

#### formProvider.reloadAllForms22+

reloadAllForms(context: UIAbilityContext): Promise<number>

Reloads all widgets. Invoked in the main process of the application, this API notifies the FormExtension process to perform batch updates of all widgets added to the current application. It can only be called within a [UIAbility](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) and uses a promise to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | [UIAbility](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) context, which is used for verification. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of widgets requested for update. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../error-codes/widget-error-codes/document.md).

| Error Code ID | Error Message |
| :-- | :-- |
| 16501000 | An internal functional error occurred. |

**Example**

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider } from '@kit.FormKit';

try {
  // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
  let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  formProvider.reloadAllForms(context).then((reloadNum: number) => {
    console.info(\`reloadAllForms success, reload number: ${reloadNum}\`);
  }).catch((error: BusinessError) => {
    console.error(\`promise error, code: ${error.code}, message: ${error.message})\`);
  });
} catch (error) {
  console.error(\`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
}
