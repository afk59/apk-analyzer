# DriverExtensionContext

The **DriverExtensionContext** module provides the context of **DriverExtensionAbility**. It inherits from **ExtensionContext**.

The **DriverExtensionContext** module provides the operations that need to be actively initiated in the **DriverExtensionAbility** implementation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/66MW4Vq7RrG1_2wP8Z-Idg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E31B5C591D5C88885BFAE194911E3439742611D0AB309A9AA140DDB9F47FD695)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### How to Use

Before using **DriverExtensionContext**, you need to obtain it through a **DriverExtensionAbility** child class instance.

  import { DriverExtensionAbility, DriverExtensionContext } from '@kit.DriverDevelopmentKit';

  let context : DriverExtensionContext | undefined;
  class EntryAbility extends DriverExtensionAbility {
    onInit() {
      context = this.context; // Obtain DriverExtensionContext.
    }
  }

#### DriverExtensionContext.updateDriverState

updateDriverState(): void

Updates the driver state. This interface is reserved and does not provide specific functionality currently.

**System capability**: SystemCapability.Driver.ExternalDevice

**Example**

// The current code implementation depends on the code implementation in the previous section.
if (context != null) {
  context.updateDriverState();
}
