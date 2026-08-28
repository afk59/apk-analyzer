# Displaying the Follow Component by API Calls

#### Use Case

Scenario Fusion Kit supports the follow component API since version 6.0.1(21).

This API allows users to follow a business account. By calling this API, your app or atomic service can display the business account follow button. Users can tap it to follow the corresponding business account.

-   If a user successfully follows an account, the button will be dimmed and the entire component will disappear 1.5 seconds later.
-   If the user fails to follow the account, an error will be reported.

#### Prerequisites

Go to the business account management console on HUAWEI Developers, apply for a business account, and obtain the account ID.

1.  Go to the business account management console, sign in with your enterprise developer account, and complete enterprise certification.
2.  Apply for a business account and complete certification.
3.  Ensure that your atomic service or app and applied business account belong to the same developer account.

#### API Description

The following table describes the API of the follow component. For other APIs, please refer to [atomicService (Convergent Scenario-specific APIs)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[showFollowComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section13456131695414)(ctx: [UIContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-api#uicontext), params: [FollowComponentParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section1881114501476), callback: [FollowComponentCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section137361343174413)): Promise<void>

 | 

Displays the follow component.

 |

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    **import { atomicService } from '@kit.ScenarioFusionKit';**
    **import { hilog } from '@kit.PerformanceAnalysisKit';**
    **import { BusinessError } from '@kit.BasicServicesKit';**
    
2.  On the target page, call the API to display the follow component. The sample code is as follows:
    
    @Entry
    @Component
    struct Index {
      aboutToAppear(): void {
        // One-tap follow component.
        // **pubId**: business account ID. The following uses the business account ID of Huawei's official assistant as an example.
        const pubId: string = '0cca1c645526449fb89d4a83e3bc25df';
        // **channelId**: channel ID. The value contains a maximum of 32 characters and can contain only digits and letters. **offset**: coordinates of the follow component.
        const params: atomicService.FollowComponentParams =
          { pubId: pubId, channelId: '', offset: { x: 0, y: 300 } };
        // Callback triggered when the follow button is tapped.
        const callbacks: atomicService.FollowComponentCallback = {
          onFollowComplete: (err, result) => {
            if (err) {
              // Error processing.
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
              return;
            }
            hilog.info(0x0000, "testTag", "follow result: %{public}d", result.code);
            if (result.code === atomicService.FollowResult.SUCCESS) {
              hilog.info(0x0000, "testTag", "follow succeeded handle");
            } else {
              hilog.info(0x0000, "testTag", "follow failed handle");
            }
          }
        }
        // Display the follow component.
        atomicService.showFollowComponent(this.getUIContext(), params, callbacks).catch((error: BusinessError<void>) => {
          hilog.error(0x0000, 'testTag', 'showFollowComponent failReason: %{public}d %{public}s:', error.code,
            error.message);
        })
      }
    
      build() {
      }
    }
