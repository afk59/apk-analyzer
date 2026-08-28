# LiveViewLockScreenExtensionAbility

**LiveViewLockScreenExtensionAbility** is an extension ability of lock screen immersive live views, which inherits from [UIExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md). The restrictions are as follows:

-   **LiveViewLockScreenExtensionAbility** is an independent subprocess and cannot start other abilities across processes.
-   The following APIs cannot be called: notification APIs, window APIs, widget APIs, background task APIs, contact APIs, distributed data management APIs, camera APIs, NFC APIs, upload and download APIs, and cellular communication APIs

**Start version**: 5.0.0(12)

#### Module Import

import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit'; 

**Device behavior differences**: This module is supported on phones and tablets, but does not work on other devices.

#### Attributes

**Model restriction**: The attributes can be used only in the stage model.

**System capability**: SystemCapability.LiveView.LiveViewService

**Device behavior differences**: This API is supported on phones and tablets, but does not work on other devices.

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

context

 | 

[LiveViewLockScreenExtensionContext](../liveviewlockscreenextensioncontext/document.md)

 | 

No

 | 

No

 | 

Context of **LiveViewLockScreenExtensionAbility**, which inherits from [ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

 |

**Example**:

import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit'; 
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class LiveViewLockScreenExtAbility extends LiveViewLockScreenExtensionAbility {
  onCreate(): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onCreate begin.');
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onSessionCreate begin.');
    let param: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(param);

    // Parse the parameters passed from **liveViewLocalScreenAbilityParameters**.
    const parameters = want?.parameters;
    let words: string = parameters?.\['words'\] ? parameters?.\['words'\] as string : 'Hello World!';
    storage.setOrCreate('words', words);

    // Load the lock screen immersive live view page.
    session.loadContent('pages/LiveViewLockScreenPage', storage);
  }
}
