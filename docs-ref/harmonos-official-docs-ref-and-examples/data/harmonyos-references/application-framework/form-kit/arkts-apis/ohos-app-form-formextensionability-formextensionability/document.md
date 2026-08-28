# @ohos.app.form.FormExtensionAbility (FormExtensionAbility)

The **FormExtensionAbility** module provides lifecycle callbacks invoked when a widget is created, destroyed, or updated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Sl0Rz1BcSR6T2OQQVq3nGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33C3B31EB4F8F1BE69BAC3ED20972D56C91A713FC7E0A587233BAF1D6D5F3C13)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The formExtensionAbility is cleared after 10 seconds of inactivity.
    
-   The following modules cannot be referenced in the FormExtensionAbility, as doing so may cause the program to exit abnormally:
    
    -   @ohos.ability.particleAbility (ParticleAbility)
    -   @ohos.multimedia.audio (Audio Management)
    -   @ohos.multimedia.camera (Camera Management)
    -   @ohos.multimedia.media (Media)
    -   @ohos.resourceschedule.backgroundTaskManager (Background Task Management)

#### Modules to Import

import { FormExtensionAbility } from '@kit.FormKit';

#### FormExtensionAbility

Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

#### \[h2\]Attributes

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [FormExtensionContext](../application/formextensioncontext/document.md) | No | No | 
Context of the FormExtensionAbility. This context is inherited from [ExtensionContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### \[h2\]FormExtensionAbility.onAddForm

onAddForm(want: Want): formBindingData.FormBindingData

Called to notify the widget provider that a widget is being created.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information of the widget. You can set the **parameters** field to one or more values enumerated in [widget parameters](../ohos-app-form-forminfo-forminfo/document.md#formparam), such as widget ID, widget name, and widget style. The information must be managed as persistent data to facilitate subsequent widget update and deletion. |

**Return value**

| Type | Description |
| :-- | :-- |
| [formBindingData.FormBindingData](../ohos-app-form-formbindingdata-formbindingdata/document.md#formbindingdata) | A **formBindingData.FormBindingData** object containing the data to be displayed on the widget. |

**Example**

import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(\`FormExtensionAbility onAddForm, want: ${want.abilityName}\`);
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };

    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
}

#### \[h2\]FormExtensionAbility.onCastToNormalForm

onCastToNormalForm(formId: string): void

Called to notify the widget provider that a temporary widget has been converted to a normal one. Temporary widgets and normal widgets are concepts of the widget host. Temporary widgets have a brief existence, appearing following particular events or user interactions and vanishing automatically upon task completion. Normal widgets maintain a lasting presence, continuing to exist unless explicitly removed or altered by the user. Function widgets developed in normal cases are normal widgets. Currently, the widget host does not use temporary widgets.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget that requests to be converted to a normal one. |

**Example**

import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onCastToNormalForm(formId: string) {
    // Called to notify the widget provider that a temporary widget has been converted to a normal one. You need to perform operations as required.
    console.info(\`FormExtensionAbility onCastToNormalForm, formId: ${formId}\`);
  }
};

#### \[h2\]FormExtensionAbility.onUpdateForm

onUpdateForm(formId: string, wantParams?: Record<string, Object>): void

Called to notify the widget provider that a widget is being updated, with update parameters carried. After obtaining the latest data, your application should call [updateForm](../ohos-app-form-formprovider-formprovider/document.md#formproviderupdateform) of **formProvider** to update the widget data.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget that requests to be updated. |
| wantParams12+ | Record<string, Object> | No | Parameters used for the update. |

**Example**

import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onUpdateForm(formId: string, wantParams?: Record<string, Object>) {
    console.info(\`FormExtensionAbility onUpdateForm, formId: ${formId},
        wantPara: ${wantParams?.\['ohos.extra.param.key.host\_bg\_inverse\_color'\]}\`);
    let param: Record<string, string> = {
      'temperature': '22c',
      'time': '22:00'
    }
    let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
    formProvider.updateForm(formId, obj2).then(() => {
      console.info(\`FormExtensionAbility context updateForm\`);
    }).catch((error: BusinessError) => {
      console.error(\`FormExtensionAbility context updateForm failed, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}\`);
    });
  }
};

#### \[h2\]FormExtensionAbility.onChangeFormVisibility

onChangeFormVisibility(newStatus: Record<string, number>): void

Called to notify the widget provider that the widget visibility status is being changed.

This API is valid only for system applications when **formVisibleNotify** is set to **true**.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| newStatus | Record<string, number> | Yes | ID and visibility status of the widget to be changed. |

**Example**

import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

// According to the ArkTS specification, Object.keys and for..in... cannot be used in .ets files to obtain the key value of an object. Use the user-defined function getObjKeys instead.
// Extract this function to a .ts file and export it. Import this function to the required .ets file before using it.
function getObjKeys(obj: Object): string\[\] {
  let keys = Object.keys(obj);
  return keys;
}

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onChangeFormVisibility(newStatus: Record<string, number>) {
    console.info(\`FormExtensionAbility onChangeFormVisibility, newStatus: ${newStatus}\`);
    let param: Record<string, string> = {
      'temperature': '22c',
      'time': '22:00'
    }
    let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);

    let keys: string\[\] = getObjKeys(newStatus);

    for (let i: number = 0; i < keys.length; i++) {
      console.info(\`FormExtensionAbility onChangeFormVisibility, key: ${keys\[i\]}, value= ${newStatus\[keys\[i\]\]}\`);
      formProvider.updateForm(keys\[i\], obj2).then(() => {
        console.info('FormExtensionAbility context updateForm');
      }).catch((error: BusinessError) => {
        console.error(\`Operation updateForm failed. , code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})\`);
      });
    }
  }
};

#### \[h2\]FormExtensionAbility.onFormEvent

onFormEvent(formId: string, message: string): void

Called to instruct the widget provider to process the widget event.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget that requests the event. |
| message | string | Yes | Event message. |

**Example**

import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onFormEvent(formId: string, message: string) {
    console.info(\`FormExtensionAbility onFormEvent, formId: ${formId}, message: ${message}\`);
  }
};

#### \[h2\]FormExtensionAbility.onRemoveForm

onRemoveForm(formId: string): void

Called to notify the widget provider that a widget is being destroyed.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | ID of the widget to be destroyed. |

**Example**

import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onRemoveForm(formId: string) {
    console.info(\`FormExtensionAbility onRemoveForm, formId: ${formId}\`);
  }
};

#### \[h2\]FormExtensionAbility.onConfigurationUpdate

onConfigurationUpdate(newConfig: Configuration): void

Called when system configuration items change. The **onConfigurationUpdate** callback is triggered only when the FormExtensionAbility is alive.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| newConfig | [Configuration](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) | Yes | New configuration. |

**Example**

import { FormExtensionAbility } from '@kit.FormKit';
import { Configuration } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onConfigurationUpdate(newConfig: Configuration) {
    // This lifecycle callback is triggered only when the configuration is updated while the FormExtensionAbility is alive.
    // If no operation is performed within 10 seconds after a FormExtensionAbility instance is created, the instance will be deleted.
    console.info(\`onConfigurationUpdate, config: ${newConfig?.language}\`);
  }
};

#### \[h2\]FormExtensionAbility.onAcquireFormState

onAcquireFormState?(want: Want): formInfo.FormState

Called to notify the widget provider that the widget host is requesting the widget state. By default, the initial widget state is returned. (You can override this API as required.)

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Description of the widget state, including the bundle name, ability name, module name, and widget name. |

**Return value**

| Type | Description |
| :-- | :-- |
| [formInfo.FormState](../ohos-app-form-forminfo-forminfo/document.md#formstate) | Enumerated values of the current widget status. |

**Example**

import { FormExtensionAbility, formInfo } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAcquireFormState(want: Want) {
    console.info(\`FormExtensionAbility onAcquireFormState, want: ${want}\`);
    return formInfo.FormState.UNKNOWN;
  }
};

#### \[h2\]FormExtensionAbility.onStop12+

onStop?(): void

Called when the widget process of the widget provider exits.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.Form

**Example**

import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onStop() {
    console.info(\`FormExtensionAbility onStop\`);
  }
}

#### \[h2\]FormExtensionAbility.onFormLocationChanged20+

onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void

Called when the widget location changes.

**Atomic service API**: This API can be used in atomic services since API version 20.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |
| newFormLocation | [formInfo.FormLocation](../ohos-app-form-forminfo-forminfo/document.md#formlocation20) | Yes | Enumerated value of the latest widget location. |

**Example**

import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    let formData: Record<string, string | Object> = {
      'data': 'addForm'
    };
    return formBindingData.createFormBindingData(formData);
  }
  onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation) {
    console.info("EntryFormAbility onFormLocationChanged current location: " + newFormLocation);
  }
}

#### \[h2\]FormExtensionAbility.onSizeChanged20+

onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void

Called when the widget size changes.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| formId | string | Yes | Widget ID. |
| newDimension | [formInfo.FormDimension](../ohos-app-form-forminfo-forminfo/document.md#formdimension) | Yes | Widget dimension. For example, **Dimension\_1\_2** indicates a 1 x 2 widget. |
| newRect | [formInfo.Rect](../ohos-app-form-forminfo-forminfo/document.md#rect20) | Yes | Widget position information, including the X and Y coordinates of the widget's top-left corner, as well as its width and height. |

**Example**

import { FormExtensionAbility, formInfo } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect) {
    console.info(\`FormExtensionAbility onSizeChanged, formId: ${formId}, newDimension: ${newDimension}\`);
  }
}
