# WindowManager (Window Management)

Window management class of the reading control.

**Start version**: 5.0.0(12)

#### Module Import

import { WindowManager } from '@kit.SpeechKit';

#### setWindowStage

static setWindowStage(windowStage: window.WindowStage): void

Sets the window manager. This API must be called in the **onWindowStageCreate** method of **EntryAbility**. Otherwise, the reading control will fail to be initialized through [init](../textreader-reading-control/document.md#section173751154134515). For details about how to set **EntryAbility**, please refer to [UIAbility Lifecycle](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-lifecycle).

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Device behavior differences**: This API is supported on PCs/2-in-1 devices, but does not work on other devices.

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

windowStage

 | 

[window.WindowStage](../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md)

 | 

Yes

 | 

Window manager, which manages each basic window unit, that is, each [Window](../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md) instance.

 |

**Example**:

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { WindowManager } from '@kit.SpeechKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    WindowManager.setWindowStage(windowStage);

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err) {
        hilog.error(0x0000, 'testTag', \`Failed to load the content. Code: ${err.code}, message: ${err.message}.\`);
        return;
      }
      hilog.info(0x0000, 'testTag', \`Succeeded in loading the content. Data: ${JSON.stringify(data)}.\` );
    });
  }

  onWindowStageDestroy(): void {
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(0x0000, 'testTag', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(0x0000, 'testTag', 'Ability onBackground');
  }
}

#### getWindowStage

static getWindowStage(): window.WindowStage

Obtains the window manager.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[window.WindowStage](../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md)

 | 

Window manager, which manages each basic window unit, that is, each [Window](../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md) instance.

 |

**Example**:

import { WindowManager } from '@kit.SpeechKit';

try {
  let windowManager = WindowManager.getWindowStage()
  console.info(\`TextReader succeeded in getting windowStage.\`)
} catch (e) {
  console.error(\`TextReader failed to get windowStage. Code: ${e.code}, message: ${e.message}.\`)
}
