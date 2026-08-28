# @ohos.InputMethodExtensionContext (InputMethodExtensionContext)

The **InputMethodExtensionContext** module, inherited from **ExtensionContext**, provides context for **InputMethodExtension** abilities. You can use the APIs of this module to start, terminate, connect, and disconnect abilities.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/4na-eEAJR9yMWsjDrewL1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53E7D2FE8428C0C526B02F466C05161C4FD0A97D4EA468897865E5B964AF84B6)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### Modules to Import

import { InputMethodExtensionContext } from '@kit.IMEKit';

#### Usage

Before using the **InputMethodExtensionContext** module, you must define a child class that inherits from **InputMethodExtensionAbility**.

import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    let context: InputMethodExtensionContext = this.context;
  }
}

#### InputMethodExtensionContext.destroy

destroy(callback: AsyncCallback<void>): void;

Destroys this input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    let context: InputMethodExtensionContext = this.context;
  }

  onDestroy() {
    this.context.destroy((err: BusinessError) => {
      if (err) {
        console.error(\`Failed to destroy context, err code = ${err.code}\`);
        return;
      }
      console.info('Succeeded in destroying context.');
    });
  }
}

#### InputMethodExtensionContext.destroy

destroy(): Promise<void>;

Destroys this input method. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    let context: InputMethodExtensionContext = this.context;
  }

  onDestroy() {
    this.context.destroy().then(() => {
      console.info('Succeed in destroying context.');
    }).catch((err: BusinessError)=>{
      console.error(\`Failed to destroy context, err code = ${err.code}\`);
    });
  }
}

#### InputMethodExtensionContext.startAbility12+

startAbility(want: Want): Promise<void>;

Starts an ability. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information, including the ability name and bundle name of the target application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md), [Ability Error Codes](../../../ability-kit/error-codes/ability-error-codes/document.md), and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000061 | Operation not supported. |
| 16200001 | The caller has been released. |
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |

**Example**

import { InputMethodExtensionAbility, InputMethodExtensionContext } from '@kit.IMEKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

class InputMethodExtAbility extends InputMethodExtensionAbility {
  onCreate(want: Want): void {
    const context: InputMethodExtensionContext = this.context;
    const targetWant: Want = {
      bundleName: "com.example.aafwk.test",
      abilityName: "com.example.aafwk.test.TwoAbility"
    };

    context.startAbility(targetWant)
      .then(() => console.info('startAbility success'))
      .catch((err: BusinessError) => {
        console.error(\`StartAbility failed. Code: ${err.code}, Message: ${err.message}\`);
      });
  }

  onDestroy() {
    this.context.destroy().then(() => {
      console.info('Succeed in destroying context.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to destroy context, err code = ${err.code}\`);
    });
  }
}
