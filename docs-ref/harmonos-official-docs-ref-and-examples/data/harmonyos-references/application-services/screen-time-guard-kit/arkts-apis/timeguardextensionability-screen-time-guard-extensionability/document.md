# TimeGuardExtensionAbility (Screen Time Guard ExtensionAbility)

**TimeGuardExtensionAbility** is the extension ability of Screen Time Guard Kit. It provides callbacks, allowing you to execute specific logic when strategies start or stop, and when users grant or revoke authorization to your app. **TimeGuardExtensionAbility** inherits from [ExtensionAbility](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

#### Module Import

import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

#### Attributes

**Model restriction**: The attributes can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

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

[TimeGuardExtensionContext](../timeguardextensioncontext-screen-time-guard-extensioncontext/document.md)

 | 

No

 | 

No

 | 

[TimeGuardExtensionContext](../timeguardextensioncontext-screen-time-guard-extensioncontext/document.md), which inherits from [ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

 |

#### onStart

onStart(strategyName: string): Promise<void>

Callback triggered when a strategy starts. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

strategyName

 | 

string

 | 

Yes

 | 

Screen time guard strategy name. The value can contain a maximum of 64 characters, and only letters, digits, and underscores (\_) are supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Example**:

import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStart(strategyName: string): Promise<void> {
    console.info('test --- onStart', strategyName, index++);
  }
}

#### onStop

onStop(strategyName: string): Promise<void>

Callback triggered when a strategy stops. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

strategyName

 | 

string

 | 

Yes

 | 

Screen time guard strategy name. The value can contain a maximum of 64 characters, and only letters, digits, and underscores (\_) are supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Example**:

import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStop(strategyName: string): Promise<void> {
    console.info('test --- onStop', strategyName, index++);
  }
}

#### onUserAuthSwitchOn

onUserAuthSwitchOn(): Promise<void>

Callback triggered when a user authorizes your app under **Settings** > **Digital Balance** > **Apps with access to Digital Balance**. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Example**:

import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOn(): Promise<void> {
    console.info('test --- onUserAuthSwitchOn', this.context, index++);
  }
}

#### onUserAuthSwitchOff

onUserAuthSwitchOff(): Promise<void>

Callback triggered when a user revokes authorization for your app under **Settings** > **Digital Balance** > **Apps with access to Digital Balance**. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.ScreenTimeGuard.GuardService

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

 |

**Example**:

import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOff(): Promise<void> {
    console.info('test --- onUserAuthSwitchOff', this.context, index++);
  }
}
