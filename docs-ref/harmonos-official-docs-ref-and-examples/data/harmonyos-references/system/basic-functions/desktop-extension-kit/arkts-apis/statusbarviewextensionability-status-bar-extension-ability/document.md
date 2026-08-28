# StatusBarViewExtensionAbility (Status Bar Extension Ability)

**StatusBarViewExtensionAbility** is inherited from [UIExtensionAbility](../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md#uiextensionability). It allows apps to integrate the ability of displaying a pop-up window when users click its icon in the status bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/PiAr7_fPR2aQ1ZKCIx6ARQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10F7E829C19BFD23DD8AB44E003EEDCE9CD48C0AA8594466F9DCB94A56A76330)

-   The APIs of this module can be used only in the stage model.

**System capability**: SystemCapability.PCService.StatusBarManager

**Start version**: 5.0.0(12)

#### Module Import

import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';

**Example:**

import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

let TAG = "MyStatusBarViewAbility";

export default class MyStatusBarViewAbility extends StatusBarViewExtensionAbility {
  onCreate() {
    console.info(TAG, \`onCreate\`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, \`onSessionCreate, want: ${want.abilityName}\`);
    session.loadContent('pages/Index');
  }

  onForeground() {
    console.info(TAG, \`onForeground\`);
  }

  onBackground() {
    console.info(TAG, \`onBackground\`);
  }

  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(TAG, \`onSessionDestroy\`);
  }

  onDestroy() {
    console.info(TAG, \`onDestroy\`);
  }
}
