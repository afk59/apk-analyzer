# FormExtensionContext

The FormExtensionContext module, inherited from [ExtensionContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md), provides the context environment for the [FormExtensionAbility](../../ohos-app-form-formextensionability-formextensionability/document.md).

You can use the APIs of this module to start a FormExtensionAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/Ile_0LQQRum72KLI-n7ddg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A67F7963506DCFEB525F6CDBEB3401F7720411E75EAD217FC11A388506970795)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### How to Use

FormExtensionContext provides information about a FormExtensionAbility, module, and HAP. You can use the information based on service requirements.

import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(\`FormExtensionAbility onAddForm, want: ${want.abilityName}\`);
    let formData: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    console.info("current language is: ", this.context.config.language);
    return formBindingData.createFormBindingData(formData);
  }
};

#### FormExtensionContext

**FormExtensionContext** is the context of [FormExtensionAbility](../../ohos-app-form-formextensionability-formextensionability/document.md).

**System capability**: SystemCapability.Ability.Form

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 11.
