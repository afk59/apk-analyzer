# FunctionComponent

Agent Framework Kit provides the capability of starting a specified agent.

After the agent for an app is launched on the [Celia open platform](https://developer.huawei.com/consumer/cn/hag/hagindex.html?isInFrame=true&amp;lang=zh_CN#/), users can enjoy the combined "app + agent" service. They can start the agent on demand through the UI control capability provided by Agent Framework Kit. For details about how to configure an agent, please refer to [Quickly Creating an Agent](https://developer.huawei.com/consumer/cn/doc/service/quick-start-0000002469548009).

**Start version**: 6.0.0(20)

#### Module Import

import { AgentController, BaseOptions, FunctionController, FunctionOptions, ButtonType, FunctionComponent } from '@kit.AgentFrameworkKit';

#### FunctionComponent

Agent function component, which can start an agent.

**Decorator type**: @Component

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

agentId

 | 

string

 | 

Yes

 | 

\-

 | 

Agent ID, which is the unique ID of an agent and is generated [when the agent is created](https://developer.huawei.com/consumer/cn/doc/service/quick-start-0000002469548009). After the agent is created, you can obtain its agent ID from the URL of the agent configuration page.

The value contains 1 to 64 characters.

 |
| 

onError

 | 

[ErrorCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

Yes

 | 

\-

 | 

Error callback function.

 |
| 

options

 | 

[FunctionOptions](#section13411955155613)

 | 

No

 | 

\-

 | 

Optional parameters for Function component initialization.

 |
| 

controller

 | 

[FunctionController](#section53411946183318)

 | 

No

 | 

\-

 | 

Function component controller. The default value is **undefined**.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1022400010

 | 

Parameter error.

 |
| 

1022400014

 | 

Internal error.

 |

**Example**:

import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";
import { FunctionComponent } from '@kit.AgentFrameworkKit';

@Entry
@Component
struct FunctionExample {
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';

  build() {
    Column() {
      FunctionComponent({
        agentId: this.agentId,
        onError: (err: BusinessError) => {
          hilog.error(0x0001, 'FunctionExample', \`err code: ${err.code}, message: ${err.message}\`)          
        },
        options: {
           title: 'Intelligent creation',
           queryText: 'Create a pattern',
           isShowShadow: true
        }
      })
    }
  }
}

#### AgentController

General controller of Agent Framework Kit controls.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

#### \[h2\]isAgentSupport

isAgentSupport(context: common.UIAbilityContext, agentId: string): Promise<boolean>

Checks for an agent's availability and returns its information if it is available. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

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

context

 | 

[common.UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#uiabilitycontext)

 | 

Yes

 | 

Context.

 |
| 

agentId

 | 

string

 | 

Yes

 | 

Agent ID, which is the unique ID of an agent and is generated [when the agent is created](https://developer.huawei.com/consumer/cn/doc/service/quick-start-0000002469548009).

The value contains 1 to 64 characters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object, which indicates whether **agentId** is valid and the agent function is supported.

**true**: yes

**false**: no

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1022400010

 | 

Parameter error.

 |
| 

1022400011

 | 

Privacy agreement not accepted.

 |
| 

1022400012

 | 

HUAWEI ID not signed in.

 |
| 

1022400013

 | 

Internet error.

 |
| 

1022400014

 | 

Internal error.

 |

**Example**:

import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";
import { common } from "@kit.AbilityKit";
import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

@Entry
@Component
struct AgentDemo {
  private functionController: FunctionController = new FunctionController()
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';
  
  @State isAgentSupport: boolean = false;

  aboutToAppear() {
     void this.checkAgentSupport()
  }

  async checkAgentSupport() {
    try {
      let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
      this.isAgentSupport = await this.functionController.isAgentSupport(context, this.agentId)
    } catch (err) {
      hilog.error(0x0001, 'AgentExample', \`err code: ${err.code}, message: ${err.message}\`)
    }
  }
  build() {
    Column() {
      // If this method is used to check whether the agent can be loaded, ensure that **agentId** is valid.
      if (this.isAgentSupport) {
        FunctionComponent({
          agentId: this.agentId,
          onError: (err: BusinessError) => {
            hilog.error(0x0001, 'AgentExample', \`err: ${JSON.stringify(err)}, message: ${err.message}\`) 
          },
          options: {
              title: 'Intelligent creation',
              queryText: 'Create a pattern',
              isShowShadow: true
          }
        })
      }
    }
  }
}

#### \[h2\]on('agentDialogOpened')

on(type: 'agentDialogOpened', callback: Callback<void>): void

Listens for the event of opening the agent pop-up.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

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

type

 | 

string

 | 

Yes

 | 

Listens for the event of opening the agent pop-up. The value is **agentDialogOpened**.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function.

 |

**Example**:

import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";
import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

@Entry
@Component
struct AgentDemo{
  private controller: FunctionController = new FunctionController();
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';

  aboutToAppear() {
    this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
    this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
  }
  onAgentOpenedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
  }
  onAgentClosedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
  }
  aboutToDisappear() {
    this.controller?.off('agentDialogOpened')
    this.controller?.off('agentDialogClosed')
  }
  build() {
    Column() {
      FunctionComponent({
        agentId: this.agentId,
        onError: (err: BusinessError) => {
          hilog.error(0x0001, 'AgentExample', \`err: ${JSON.stringify(err)}, message: ${err.message}\`) 
        },
        options: {
          title: 'Intelligent creation',
          queryText: 'Create a pattern',
          isShowShadow: true
        },
        controller: this.controller
      })
    }
  }
}

#### \[h2\]off('agentDialogOpened')

off(type: 'agentDialogOpened', callback?: Callback<void>): void

Cancels the listening for the event of opening the agent pop-up.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

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

type

 | 

string

 | 

Yes

 | 

Cancels the listening for the event of opening the agent pop-up. The value is **agentDialogOpened**.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function to be unregistered, which must the same as that passed upon subscription. If this parameter is not passed, all callback functions are unregistered.

 |

**Example**:

import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";
import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

@Entry
@Component
struct AgentDemo{
  private controller: FunctionController = new FunctionController();
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';

  aboutToAppear() {
    this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
    this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
  }
  onAgentOpenedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
  }
  onAgentClosedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
  }
  aboutToDisappear() {
    this.controller?.off('agentDialogOpened')
    this.controller?.off('agentDialogClosed')
  }
  build() {
    Column() {
      FunctionComponent({
        agentId: this.agentId,
        onError: (err: BusinessError) => {
          hilog.error(0x0001, 'AgentExample', \`err: ${JSON.stringify(err)}, message: ${err.message}\`) 
        },
        options: {
          title: 'Intelligent creation',
          queryText: 'Create a pattern',
          isShowShadow: true
        },
        controller: this.controller
      })
    }
  }
}

#### \[h2\]on('agentDialogClosed')

on(type: 'agentDialogClosed', callback: Callback<void>): void

Listens for the event of closing the agent pop-up.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

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

type

 | 

string

 | 

Yes

 | 

Listens for the event of closing the agent pop-up. The value is **agentDialogClosed**.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function.

 |

**Example**:

import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";
import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

@Entry
@Component
struct AgentDemo{
  private controller: FunctionController = new FunctionController();
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';

  aboutToAppear() {
    this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
    this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
  }
  onAgentOpenedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
  }
  onAgentClosedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
  }
  aboutToDisappear() {
    this.controller?.off('agentDialogOpened')
    this.controller?.off('agentDialogClosed')
  }
  build() {
    Column() {
      FunctionComponent({
        agentId: this.agentId,
        onError: (err: BusinessError) => {
          hilog.error(0x0001, 'AgentExample', \`err: ${JSON.stringify(err)}, message: ${err.message}\`) 
        },
        options: {
          title: 'Intelligent creation',
          queryText: 'Create a pattern',
          isShowShadow: true
        },
        controller: this.controller
      })
    }
  }
}

#### \[h2\]off('agentDialogClosed')

off(type: 'agentDialogClosed', callback?: Callback<void>): void

Cancels the listening for the event of closing the agent pop-up.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

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

type

 | 

string

 | 

Yes

 | 

Cancels the listening for the event of closing the agent pop-up. The value is **agentDialogClosed**.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function to be unregistered, which must the same as that passed upon subscription. If this parameter is not passed, all callback functions are unregistered.

 |

**Example**:

import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";
import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';

@Entry
@Component
struct AgentDemo{
  private controller: FunctionController = new FunctionController();
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';

  aboutToAppear() {
    this.controller?.on('agentDialogOpened', this.onAgentOpenedCallback)
    this.controller?.on('agentDialogClosed', this.onAgentClosedCallback)
  }
  onAgentOpenedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog opened callback')
  }
  onAgentClosedCallback = () => {
    hilog.info(0x0001, 'AgentExample', 'agent dialog closed callback')
  }
  aboutToDisappear() {
    this.controller?.off('agentDialogOpened')
    this.controller?.off('agentDialogClosed')
  }
  build() {
    Column() {
      FunctionComponent({
        agentId: this.agentId,
        onError: (err: BusinessError) => {
          hilog.error(0x0001, 'AgentExample', \`err: ${JSON.stringify(err)}, message: ${err.message}\`) 
        },
        options: {
          title: 'Intelligent creation',
          queryText: 'Create a pattern',
          isShowShadow: true
        },
        controller: this.controller
      })
    }
  }
}

#### FunctionController

Function component controller, which is used to control the interactions with Function components. This API is reserved. In the current version, this API inherits from [AgentController](#section37192953318)'s methods without any additional implementation.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

#### BaseOptions

Basic object of optional component parameters.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

**Parameters**:

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

title

 | 

string

 | 

No

 | 

Yes

 | 

Title of the AgentFramework component. By default, the parameter value is null.

This parameter does not take effect when [FunctionOptions](#section13411955155613).buttonType is **ButtonType.CIRCLE**.

Currently, only a maximum of eight Chinese characters can be displayed. Characters beyond this limit will be truncated.

If the font scale is greater than 1.75x, a maximum of two lines can be displayed by default.

 |
| 

titleFontSize

 | 

number

 | 

No

 | 

Yes

 | 

Font size of the AgentFramework component title. The value range is \[14, 16\]. The default value is **16**. For values out of this range, the default value will be used.

 |
| 

iconSize

 | 

number

 | 

No

 | 

Yes

 | 

Icon size of the AgentFramework component. The value range is \[16, 24\].

-   When the button type is **CIRCLE**, the default value is **24**.
-   When the button type is **CAPSULE**, the default value is **20**.

For values out of this range, the default value will be used.

 |
| 

iconColors

 | 

[ResourceColor\[\]](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Icon color. Currently, only one color is supported. If this parameter is not set, the default gradient icon is used.

 |

#### FunctionOptions

Function component options. This API inherits from [BaseOptions](#section1671758531).

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

**Parameters**:

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

queryText

 | 

string

 | 

No

 | 

Yes

 | 

Initial query text to use the Function component. By default, this parameter is null.

 |
| 

controlSize

 | 

[ControlSize](../../../../application-framework/arkui/arkts-components/buttons-and-selections/button/document.md#controlsize11-1)

 | 

No

 | 

Yes

 | 

Button size of the Function component. The default value is **ControlSize.NORMAL**.

 |
| 

buttonType

 | 

[ButtonType](#section10388117018)

 | 

No

 | 

Yes

 | 

Button type of the Function component. If the **title** attribute is null or not set, the default value is **ButtonType.CIRCLE**. If the **title** attribute is not null, the default value is **ButtonType.CAPSULE**.

 |
| 

isShowShadow

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the button shadow. It is valid only for capsule buttons (**ButtonType.CAPSULE**). The default value is **false**.

**true**: yes

**false**: no

 |
| 

backgroundColor

 | 

[ResourceColor](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of the component with a background panel.

The default value is **sys.color.comp\_background\_tertiary**.

 |
| 

titleColors

 | 

[ResourceColor\[\]](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Function component text color. Currently, a maximum of two colors can be set.

-   Setting two colors will create a gradient effect.
-   Setting one color will apply a solid color
-   If no color is set, the default gradient color is used.

 |

#### ButtonType

Enumeration values of the button type.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**System capability**: SystemCapability.AI.Agent.AgentKit

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CIRCLE

 | 

0

 | 

Circle button.

 |
| 

CAPSULE

 | 

1

 | 

Capsule button (with a default corner radius of half its height).

NOTE:

A capsule button is displayed when the font scale is less than 1.75x. Otherwise, a rounded-rectangular button is displayed.

 |
| 

ICON\_ABOVE\_TITLE

 | 

2

 | 

Capsule button where the icon is stacked above the title.

**Start version**: 6.0.1(21)

 |
