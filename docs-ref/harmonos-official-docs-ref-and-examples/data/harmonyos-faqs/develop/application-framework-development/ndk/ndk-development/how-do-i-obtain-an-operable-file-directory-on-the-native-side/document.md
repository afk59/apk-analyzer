# How do I obtain an operable file directory on the native side?

There is no native API for directly obtaining file directories. You can obtain the path information from ArkTS and pass it to native.

Sample code:

import { common } from '@kit.AbilityKit';

const context = AppStorage.get("context") as UIContext;
let hostContext = context.getHostContext() as common.UIAbilityContext;
let filesDir = hostContext.filesDir;
