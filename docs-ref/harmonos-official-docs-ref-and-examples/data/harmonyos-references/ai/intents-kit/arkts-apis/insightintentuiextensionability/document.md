# InsightIntentUIExtensionAbility

**InsightIntentUIExtensionAbility** is used to display information during intent calls in AI Voice. It provides UI extension capabilities for intent calls. Your app can declare one or more **InsightIntentUI** objects to present intents on a windowed UI. **InsightIntentUIExtensionAbility** extends [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md).

**Start version**: 5.0.0(12)

#### Module Import

import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';

#### InsightIntentUIExtensionAbility

**Model restriction**: This class can be used only in the stage model.

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 5.0.0(12)

#### Example

import { InsightIntentUIExtensionAbility } from '@kit.IntentsKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

// In this example, **TestUiExtAbility** extends **InsightIntentUIExtensionAbility**.
export default class TestUiExtAbility extends InsightIntentUIExtensionAbility {
    onCreate() {
    }

    onForeground() {
    }

    onBackground() {
    }

    onDestroy() {
    }

    onSessionCreate(want: Want, session: UIExtensionContentSession) {
    }

    onSessionDestroy(session: UIExtensionContentSession) {
    }
}
