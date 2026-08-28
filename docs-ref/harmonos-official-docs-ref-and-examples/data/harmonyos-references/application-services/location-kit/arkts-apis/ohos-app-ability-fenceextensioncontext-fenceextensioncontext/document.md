# @ohos.app.ability.FenceExtensionContext (FenceExtensionContext)

The **FenceExtensionContext** class defines the context for **FenceExtensionAbility** objects. Inherited from [ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md), this class provides the configuration information of **FenceExtensionAbility** objects and the API for starting them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/E0zmn3R0Qme9-tSTUXqjtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AB31BDAE2F1EE95DB5A5F46DBEA23D5680DF0A60966A0AF3381834574A659C3)

The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { FenceExtensionContext } from '@kit.LocationKit';

#### How to Use

Before using **FenceExtensionContext**, you must first obtain a **FenceExtensionAbility** instance.

import { FenceExtensionAbility, FenceExtensionContext } from '@kit.LocationKit';

class MyFenceExtensionAbility extends FenceExtensionAbility {
  onCreate() {
    let fenceExtensionContext: FenceExtensionContext = this.context;
  }
}
