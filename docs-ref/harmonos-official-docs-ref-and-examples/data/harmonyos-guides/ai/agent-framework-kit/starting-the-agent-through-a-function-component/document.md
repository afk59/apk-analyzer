# Starting the Agent Through a Function Component

#### Use Cases

-   Function components include the icon component and button component. When no title is set, the icon component is displayed by default. When a title is set, the button component is displayed by default.
-   Icon component: comprehensive entry. It contains no user intent and can function as the main entry of the agent in an app.
    
-   Button component: provides an entry to the agent along with a custom function description.
    

#### Preparations

-   Create an agent. For details, please refer to [Quickly Creating an Agent](https://developer.huawei.com/consumer/cn/doc/service/quick-start-0000002469548009).
-   Associate the agent with an app. For details, please refer to [Associating an App](https://developer.huawei.com/consumer/cn/doc/service/related-applications-0000002437785706).
-   Ensure that a HUAWEI ID has been signed in on the device and the device is connected to the Internet.

#### Development Procedure

1.  In the **/src/main/ets/pages/Index.ets** file of the project root directory, import **FunctionComponent** and related classes.
    
    import { FunctionComponent, FunctionController } from '@kit.AgentFrameworkKit';
    import { BusinessError } from "@kit.BasicServicesKit";
    import { hilog } from "@kit.PerformanceAnalysisKit";
    import { common } from '@kit.AbilityKit'
    
2.  (Optional) Call [isAgentSupport](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hmaf-function-component#section123851974413) to check whether the current agent ID is available before component loading. Load the component only when the agent ID is available and the agent function is supported.
    
      @State isAgentSupport: boolean = false;
      
      aboutToAppear() {
         this.checkAgentSupport()
      }
      async checkAgentSupport() {
        try {
          let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
          this.isAgentSupport = await this.controller.isAgentSupport(context, this.agentId)
        } catch (err) {
          hilog.error(0x0001, 'AgentExample', \`err code: ${err.code}, message: ${err.message}\`)
        }
      }
    
      build() {
        Column() {
          if (this.isAgentSupport) {
            FunctionComponent({
              agentId: this.agentId,
              onError: (err: BusinessError) => {
                hilog.error(0x0001, 'AgentExample', \`err: ${JSON.stringify(err)}, message: ${err.message}\`)
              },
              options: {
                  title: 'Intelligent creation',
                  queryText: 'Create a pattern'
              }
            })
          }
        }
      }
    
3.  Build a simple configuration screen, use **FunctionComponent** on this screen, and pass the required parameters to the component. The **agentId** and **onError** parameters are mandatory. For details about optional parameters, please refer to [FunctionComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hmaf-function-component). For details about the **FunctionComponent** layout, please refer to [Component Layouts](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/component-layouts/document.md).
    
      @Entry
      @Component
      export struct AgentExample {
        private controller: FunctionController = new FunctionController();
        private agentId: string = 'agentproxy65481da1fa2293a8482d45';
        build() {
          Column() {
            FunctionComponent({
              agentId: this.agentId,
              onError: (err: BusinessError) => {
                hilog.error(0x0001, 'AgentExample', \`err: ${JSON.stringify(err)}, message: ${err.message}\`) 
              },
              options: {
                title: '',
                queryText: ''
              },
              controller: this.controller
            })
          }
        }
      }
    
4.  Add a subscription event.
    
      aboutToAppear() {
         this.initListeners()
      }
      initListeners() {
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
            controller: this.controller
          })
        }
      }
    

#### Development Example

Tap the button to open the agent pop-up.

import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";

import {
  FunctionComponent,
  FunctionController
} from "@kit.AgentFrameworkKit";

@Entry
@Component
export struct AgentExample {
  private controller: FunctionController = new FunctionController();
  private agentId: string = 'agentproxy65481da1fa2293a8482d45';

  aboutToAppear() {
    this.initListeners()
  }
  initListeners() {
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
          queryText: 'Create a scenario',
          isShowShadow: true
        },
        controller: this.controller
      })
    }
  }
}
