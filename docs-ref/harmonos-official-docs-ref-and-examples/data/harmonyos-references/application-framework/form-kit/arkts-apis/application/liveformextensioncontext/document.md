# LiveFormExtensionContext

**LiveFormExtensionContext**, inherited from [ExtensionContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md), is the context of [LiveFormExtensionAbility](../../ohos-app-form-liveformextensionability-liveformextensionability/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/2rpfYktgQYuUserpL8AM6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0147CAAEFC3F3CFC93946F6BBC7B4874DD0E006CC36CE89138DE6FA99510086F)

-   The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { common } from '@kit.AbilityKit';

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ifNvdwLSQVS2zoXw6JX7Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50D0F7630612E38D081C97E459CBDEDB7E59566FD7D59DA0153B2C29BB020541)

-   In versions earlier than API version 22, you need to import LiveFormExtensionContext with import LiveFormExtensionContext from 'application/LiveFormExtensionContext'; . This import mode is marked in red in DevEco Studio, but does not affect compilation and running. You can use LiveFormExtensionContext directly.
    
-   In API version 22 and later versions, you can import LiveFormExtensionContext with import { common } from '@kit.AbilityKit'; and use it in the form of **common.LiveFormExtensionContext**.
    

#### LiveFormExtensionContext

LiveFormExtensionContext, inherited from [ExtensionContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md), allows you to access resources specific to LiveFormExtensionAbility.

#### \[h2\]startAbilityByLiveForm

startAbilityByLiveForm(want: Want): Promise<void>

Starts the widget provider (application) page. This API uses a promise to return the result.

This API can only be used to start the page of the interactive widget provider (application). If this API is used to start the page of another application, error code 16501011 will be reported.

You are advised to call this API in click event callbacks. Calling it in callbacks of other gesture events is not recommended, and direct calls in non-gesture events are not allowed. Otherwise, the error code 16501011 will be reported.

In addition, this API can be directly called in the click event callback but cannot be called after a delay. Otherwise, the error code 16501011 will be reported.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Information about the application page to be started. [Only explicit Want is supported](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ability-startup-with-explicit-want). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Form Error Codes](../../../error-codes/widget-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported due to limited device capabilities. |
| 16500050 | An IPC connection error happened. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501011 | The form can not support this operation. |

**Example**

// MyLiveFormExtensionAbility.ets
import { formInfo, LiveFormInfo, LiveFormExtensionAbility } from '@kit.FormKit';
import { UIExtensionContentSession } from '@kit.AbilityKit';

export default class MyLiveFormExtensionAbility extends LiveFormExtensionAbility {
  onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
    // 1. Pass LiveFormExtensionContext to the widget page component.
    let storage: LocalStorage = new LocalStorage();
    storage.setOrCreate('context', this.context);
    session.loadContent('pages/MyLiveFormPage', storage);
  }
};

// pages/MyLiveFormPage.ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct MyLiveFormPage {
  private storageForMyLiveFormPage: LocalStorage | undefined = undefined;
  private liveFormContext: common.LiveFormExtensionContext | undefined = undefined;

  aboutToAppear(): void {
    // 2. Obtain LiveFormExtensionContext.
    this.storageForMyLiveFormPage = this.getUIContext().getSharedLocalStorage();
    this.liveFormContext = this.storageForMyLiveFormPage?.get<common.LiveFormExtensionContext>('context');
  }

   private startAbilityByLiveForm(): void {
    try {
      // Replace the Want information with the actual one.
      this.liveFormContext?.startAbilityByLiveForm({
        bundleName: 'com.example.liveformdemo',
        abilityName: 'EntryAbility',
      })
        .then(() => {
          console.info('startAbilityByLiveForm succeed');
        })
        .catch((err: BusinessError) => {
          console.error(\`startAbilityByLiveForm failed, code is ${err?.code}, message is ${err?.message}\`);
        });
    } catch (e) {
      console.error(\`startAbilityByLiveForm failed, code is ${e?.code}, message is ${e?.message}\`);
    }
  }

  build() {
    // Replace the page with the actual one.
    Stack() {
      Column()
        .width('50%')
        .height('50%')
        .backgroundColor('#2875F5')
    }
    .width('100%')
    .height('100%')
    .onClick(() => {
      // 3. Use the API in the click event callback.
      console.info('MyLiveFormPage click to start ability');
      if (!this.liveFormContext) {
        console.info('MyLiveFormPage liveFormContext is empty');
        return;
      }
      this.startAbilityByLiveForm();
    })
  }
}
