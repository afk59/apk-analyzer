# UIAbilityContext

UIAbilityContext provides the context environment for a [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). It inherits from [Context](../context-context-base-class-of-the-stage-model/document.md). For details about the relationships and differences between various types of contexts, see [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage).

When a UIAbility component is instantiated, the system automatically creates the corresponding UIAbilityContext. You can use the APIs provided by UIAbilityContext to obtain the ability information (AbilityInfo), application information (ApplicationInfo), and other information, start another UIAbility, connect to system services, and destroy a UIAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/h9d2UAE0S8qOHsvinwWqIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6D148FC86DA3F22391E994CAB15AE43B4F9DAF83C5B0F6221BD074950E69444)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.
-   In the sample code provided in this topic, **this.context** is used to obtain UIAbilityContext, where **this** indicates an instance that inherits from UIAbility.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### UIAbilityContext

#### \[h2\]Properties

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| abilityInfo | [AbilityInfo](../../bundlemanager/abilityinfo/document.md) | No | No | 
UIAbility information.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| currentHapModuleInfo | [HapModuleInfo](../../bundlemanager/hapmoduleinfo/document.md) | No | No | 

Information about the HAP to which the UIAbility belongs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| config | [Configuration](../../../both-models-recommended/ohos-app-ability-configuration-environment-variables/document.md) | No | No | 

Environment variables for the application runtime, such as language and color mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowStage12+ | [window.WindowStage](../../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md) | No | No | 

WindowStage object. It can be called only on the main thread.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### \[h2\]startAbility

startAbility(want: Want, callback: AsyncCallback<void>): void

Starts a UIAbility. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/NPWSRo4qQQWY24L5Oe9c4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1656370E09CF17438E85EA36E4641843A25EE84DAEDB92A1861CB877ED59237)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIAbility. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0** and **message** is an empty string. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
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
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      this.context.startAbility(want, (err: BusinessError) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbility succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]startAbility

startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void

Starts a UIAbility. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Zj1Bt67ARHK1ExEOdUtuqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=048ADF765FD07D29C9F8CBAFE7F9A243A1A8CEC3AFEDAB4E0794A63CEF12C5F3)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIAbility. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | Yes | Parameters used for starting the UIAbility. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0** and **message** is an empty string. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not support. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000067 | The StartOptions check failed. |
| 16000068 | The ability is already running. |
| 16300003 | The target application is not the current application. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbility succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]startAbility

startAbility(want: Want, options?: StartOptions): Promise<void>

Starts a UIAbility. This API uses a promise to return the result. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/q8uhrXJ7SoWkchg-kMtZZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EFFE4B2EB94288EC96C0AC146CA7A2103E334D1212D66B8BAC7F012C6F99E57)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIAbility. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | No | Parameters used for starting the UIAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not support. |
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
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000067 | The StartOptions check failed. |
| 16000068 | The ability is already running. |
| 16300003 | The target application is not the current application. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbility(want, options)
        .then(() => {
          // Carry out normal service processing.
          console.info('startAbility succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]startAbilityForResult

startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

The following situations may be possible for a started UIAbility:

-   Normally, you can call [terminateSelfWithResult](#terminateselfwithresult) to terminate the UIAbility and return the result to the caller.
-   If an exception occurs, for example, the UIAbility is killed, an exception result, in which **resultCode** is **\-1**, is returned to the caller.
-   If the UIAbility is in [singleton mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#singleton) and this UIAbility is started multiple times by different applications calling this API, when the UIAbility calls [terminateSelfWithResult](#terminateselfwithresult) to terminate itself, it will only return the normal result to the last caller. All other callers will receive an exception result with **resultCode** set to **\-1**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/CLzT1YJBQSu4FR5_CSB4Vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6D2AF0FB38E6DB717EB1A7BE4F6C2A13A348C81F691F7058BF6BBFF0268C6A3)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIAbility. |
| callback | AsyncCallback<[AbilityResult](../../ability/abilityresult/document.md)\> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0** and **data** is the result code and data when the UIAbility exits. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
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
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      this.context.startAbilityForResult(want, (err: BusinessError, result: common.AbilityResult) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbilityForResult failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbilityForResult succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbilityForResult failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]startAbilityForResult

startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

The following situations may be possible for a started UIAbility:

-   Normally, you can call [terminateSelfWithResult](#terminateselfwithresult) to terminate the UIAbility and return the result to the caller.
-   If an exception occurs, for example, the UIAbility is killed, an exception result, in which **resultCode** is **\-1**, is returned to the caller.
-   If the UIAbility is in [singleton mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#singleton) and this UIAbility is started multiple times by different applications calling this API, when the UIAbility calls [terminateSelfWithResult](#terminateselfwithresult) to terminate itself, it will only return the normal result to the last caller. All other callers will receive an exception result with **resultCode** set to **\-1**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/m5rs850ISnKwkEEndZghmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DBD7B0966535DD7A80A9DA44071B9AEC2E1143ABB0B465FC7B1FB69B49C0AC4)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIAbility. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | Yes | Parameters used for starting the UIAbility. |
| callback | AsyncCallback<[AbilityResult](../../ability/abilityresult/document.md)\> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0** and **data** is the result code and data when the UIAbility exits. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbilityForResult(want, options, (err: BusinessError, result: common.AbilityResult) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbilityForResult failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbilityForResult succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbilityForResult failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]startAbilityForResult

startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses a promise to return the result. It can be called only on the main thread.

The following situations may be possible for a started UIAbility:

-   Normally, you can call [terminateSelfWithResult](#terminateselfwithresult) to terminate the UIAbility and return the result to the caller.
-   If an exception occurs, for example, the UIAbility is killed, an exception result, in which **resultCode** is **\-1**, is returned to the caller.
-   If the UIAbility is in [singleton mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#singleton) and this UIAbility is started multiple times by different applications calling this API, when the UIAbility calls [terminateSelfWithResult](#terminateselfwithresult) to terminate itself, it will only return the normal result to the last caller. All other callers will receive an exception result with **resultCode** set to **\-1**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/CgRuI5zUSDeVGXyisACi-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=383B60B112344616A968E40F231EF49C48B9483B954A47EAE1D70DFBCEFCD1E5)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIAbility. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | No | Parameters used for starting the UIAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityResult](../../ability/abilityresult/document.md)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
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
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbilityForResult(want, options)
        .then((result: common.AbilityResult) => {
          // Carry out normal service processing.
          console.info('startAbilityForResult succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(\`startAbilityForResult failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbilityForResult failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]terminateSelf

terminateSelf(callback: AsyncCallback<void>): void

Terminates this UIAbility. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/83NrzeF3T0i1FpC7H_nqEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66B1D2A4866BC6B0C40E7637DAF0304477ABA15764673E9D605824CBFA1D870A)

After this API is called, missions in the task center are not cleared by default. To clear missions, set [removeMissionAfterTerminate](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

1.  The following is an example of calling **terminateSelf** to terminate a UIAbility. By default, the application retains the snapshot in the recent tasks list.
    
    import { UIAbility } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    export default class EntryAbility extends UIAbility {
      onForeground() {
        try {
          this.context.terminateSelf((err: BusinessError) => {
            if (err.code) {
              // Process service logic errors.
              console.error(\`terminateSelf failed, code is ${err.code}, message is ${err.message}\`);
              return;
            }
            // Carry out normal service processing.
            console.info('terminateSelf succeed');
          });
        } catch (err) {
          // Capture the synchronization parameter error.
          let code = (err as BusinessError).code;
          let message = (err as BusinessError).message;
          console.error(\`terminateSelf failed, code is ${code}, message is ${message}\`);
        }
      }
    }
    
2.  (Optional) To remove the mission from the task center (that is, not to retain the snapshot in the recent tasks list) when terminating the UIAbility, set the **removeMissionAfterTerminate** field to **true** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file.
    
    {
      "module": {
        // ...
        "abilities": \[
          {
            // ...
            "removeMissionAfterTerminate": true
          }
        \]
      }
    }
    

#### \[h2\]terminateSelf

terminateSelf(): Promise<void>

Terminates this UIAbility. This API uses a promise to return the result. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/GwyFqfqdT9qARPrx43Krsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C42E04C02A8F1124E7D16D39F9E669B0FBA6623B3D9008EE2E31D451568BEA0C)

After this API is called, missions in the task center are not cleared by default. To clear missions, set [removeMissionAfterTerminate](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

1.  The following is an example of calling **terminateSelf** to terminate a UIAbility. By default, the application retains the snapshot in the recent tasks list.
    
    import { UIAbility } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    export default class EntryAbility extends UIAbility {
      onForeground() {
        try {
          this.context.terminateSelf()
            .then(() => {
              // Carry out normal service processing.
              console.info('terminateSelf succeed');
            })
            .catch((err: BusinessError) => {
              // Process service logic errors.
              console.error(\`terminateSelf failed, code is ${err.code}, message is ${err.message}\`);
            });
        } catch (err) {
          // Capture the synchronization parameter error.
          let code = (err as BusinessError).code;
          let message = (err as BusinessError).message;
          console.error(\`terminateSelf failed, code is ${code}, message is ${message}\`);
        }
      }
    }
    
2.  (Optional) To remove the mission from the task center (that is, not to retain the snapshot in the recent tasks list) when terminating the UIAbility, set the **removeMissionAfterTerminate** field to **true** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file.
    
    {
      "module": {
        // ...
        "abilities": \[
          {
            // ...
            "removeMissionAfterTerminate": true
          }
        \]
      }
    }
    

#### \[h2\]terminateSelfWithResult

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

Terminates this UIAbility. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

The result is returned to the caller when **terminateSelfWithResult** is called to terminate the UIAbility that is started by calling [startAbilityForResult](#startabilityforresult).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/D5L3Vw7vQUacdj8HMU05QA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0599BFA342B072051C90012FBCF16E21DB2AD474B2E6C54E83077706EEF1F5B)

After this API is called, missions in the task center are not cleared by default. To clear missions, set [removeMissionAfterTerminate](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [AbilityResult](../../ability/abilityresult/document.md) | Yes | Information returned to the caller. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let resultCode = 100;
    // AbilityResult information returned to the caller.
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };

    try {
      this.context.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('terminateSelfWithResult succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`terminateSelfWithResult failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]terminateSelfWithResult

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

Terminates this UIAbility. This API uses a promise to return the result. It can be called only on the main thread.

The result is returned to the caller when **terminateSelfWithResult** is called to terminate the UIAbility that is started by calling [startAbilityForResult](#startabilityforresult).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Ru3VIaAsSr-MbezJa4AArA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70A87642383A8762A8587587F3C300B5FE7F7315497A9749378017CBD059646A)

After this API is called, missions in the task center are not cleared by default. To clear missions, set [removeMissionAfterTerminate](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) to **true**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [AbilityResult](../../ability/abilityresult/document.md) | Yes | Information returned to the caller. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let resultCode = 100;
    // AbilityResult information returned to the caller.
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };

    try {
      this.context.terminateSelfWithResult(abilityResult)
        .then(() => {
          // Carry out normal service processing.
          console.info('terminateSelfWithResult succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(\`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`terminateSelfWithResult failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]connectServiceExtensionAbility

connectServiceExtensionAbility(want: Want, options: ConnectOptions): number

Connects this UIAbility to a [ServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/extensionability-overview). It enables communication with the ServiceExtensionAbility via a proxy, allowing access to the capabilities exposed by the ServiceExtensionAbility. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/iaZDQC5wQA6RCtEjITLEQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C81C0006EC84E3B8285535250F9B34C5D0756B6D869AE484FA29C154BAEFDE7A)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information for connecting to the ServiceExtensionAbility. |
| options | [ConnectOptions](../../ability/connectoptions/document.md) | Yes | Callback used to return the information indicating that the connection is successful, failed, or interrupted. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Connection ID. A caller can call [disconnectServiceExtensionAbility](#disconnectserviceextensionability) with this ID for disconnection. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |

**Example**

import { UIAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'ServiceExtensionAbility'
    };
    let commRemote: rpc.IRemoteObject;
    let options: common.ConnectOptions = {
      onConnect(elementName, remote) {
        commRemote = remote;
        console.info('onConnect...');
      },
      onDisconnect(elementName) {
        console.info('onDisconnect...');
      },
      onFailed(code) {
        console.info('onFailed...');
      }
    };
    let connection: number;

    try {
      connection = this.context.connectServiceExtensionAbility(want, options);
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`connectServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]disconnectServiceExtensionAbility

disconnectServiceExtensionAbility(connection: number): Promise<void>

Disconnects from a [ServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/extensionability-overview). Once the connection is terminated, set the remote object, which is returned when the connection is established, to null. This API uses a promise to return the result. It can be called only on the main thread.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | ID of the connected ServiceExtensionAbility, that is, **connectionId** returned by [connectServiceExtensionAbility](#connectserviceextensionability). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    // connection is the return value of connectServiceExtensionAbility.
    let connection = 1;
    let commRemote: rpc.IRemoteObject | null;

    try {
      this.context.disconnectServiceExtensionAbility(connection).then(() => {
        commRemote = null;
        // Carry out normal service processing.
        console.info('disconnectServiceExtensionAbility succeed');
      }).catch((err: BusinessError) => {
        // Process service logic errors.
        console.error(\`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}\`);
      });
    } catch (err) {
      commRemote = null;
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]disconnectServiceExtensionAbility

disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void

Disconnects from a [ServiceExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/extensionability-overview). Once the connection is terminated, set the remote object, which is returned when the connection is established, to null. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | ID of the connected ServiceExtensionAbility, that is, **connectionId** returned by [connectServiceExtensionAbility](#connectserviceextensionability). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    // connection is the return value of connectServiceExtensionAbility.
    let connection = 1;
    let commRemote: rpc.IRemoteObject | null;

    try {
      this.context.disconnectServiceExtensionAbility(connection, (err: BusinessError) => {
        commRemote = null;
        if (err.code) {
          // Process service logic errors.
          console.error(\`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('disconnectServiceExtensionAbility succeed');
      });
    } catch (err) {
      commRemote = null;
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]startAbilityByCall

startAbilityByCall(want: Want): Promise<Caller>

Obtains a [Caller](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#caller) object for communicating with a [Callee](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#callee) object. If the specified UIAbility is not started, the UIAbility will be started in the foreground or background. This API uses a promise to return the result. It can be called only on the main thread.

This API cannot be used to start the UIAbility with the launch type set to [specified](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#specified).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/-M_uFwCfRVuPTIj1xxA44w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=979A1C3E09350AB3D4FA712B913870A48785B7AC34897714E6D3F11959D11033)

-   In cross-device scenarios, the caller and the callee must belong to the same application.
    
-   In same-device scenarios, the caller and the callee must belong to different applications, and the caller must have the ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION permission (available only for system applications).
    
-   In addition, if the application needs to call this API in the background, the ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND permission is required (available only for system applications). For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).
    

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/2V5O26ymR2uumppHciA1tA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=120B4FECF14DFE9E58C879CA891632304920F5BF8E44DB2606BDE2878A97C057)

-   For API version 10 and earlier, the permission ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION is required. This permission is available only to system applications.
    
-   For API version 11 and later, only the permission ohos.permission.DISTRIBUTED\_DATASYNC is required. This permission is verified by the DSoftBus subsystem only when the link between applications is established. No verification is conducted during the application launch phase.
    

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Information about the UIAbility to start, including the ability name, module name, bundle name, device ID, and parameters (optional). If **'ohos.aafwk.param.callAbilityToForeground'** in **parameters** is set to **true**, the UIAbility is brought to the foreground. Otherwise, the UIAbility is brought to the background. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Caller](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#caller)\> | Promise used to return the Caller object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed. 2.Sending restart message to system service failed. 3.System service failed to communicate with dependency module. 4.Non-system applications are only allowed to call this interface across devices, not on the current device. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |

**Example**

The following code demonstrates that the caller launches the callee to the background, sends a message to the callee after successfully obtaining the Caller object, and then releases the Caller object.

import { Caller, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rpc } from '@kit.IPCKit';

const DOMAIN = 0x0000;
const LOG\_TAG = 'TEST\_TAG';

class TestParcelable implements rpc.Parcelable {
  age: number = 0;
  name: string = '';
  marshalling(dataOut: rpc.MessageSequence): boolean {
    dataOut.writeInt(this.age);
    dataOut.writeString(this.name);
    return true;
  }
  unmarshalling(dataIn: rpc.MessageSequence): boolean {
    this.age = dataIn.readInt();
    this.name = dataIn.readString();
    return true;
  }
}

export default class EntryAbility extends UIAbility {
  async onForeground() {
    let caller: Caller;
    // Start the ability in the background.
    let wantBackground: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
    };

    try {
      caller = await this.context.startAbilityByCall(wantBackground);
      await caller.call('TEST\_CALL', new TestParcelable());
      caller.release();
    } catch (err) {
      // Process input parameter errors.
      hilog.error(DOMAIN, LOG\_TAG, \`startAbilityByCall failed ${err}\`);
    }
  }
}

The following code demonstrates that the callee registers a listener after being launched and unregisters the listener when destroyed.

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rpc } from '@kit.IPCKit';

const DOMAIN = 0x0000;
const LOG\_TAG = 'TEST\_TAG';

class TestParcelable implements rpc.Parcelable {
  age: number = 0;
  name: string = '';
  marshalling(dataOut: rpc.MessageSequence): boolean {
    dataOut.writeInt(this.age);
    dataOut.writeString(this.name);
    return true;
  }
  unmarshalling(dataIn: rpc.MessageSequence): boolean {
    this.age = dataIn.readInt();
    this.name = dataIn.readString();
    return true;
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, LOG\_TAG, '%{public}s', 'Ability onCreate');
    // Register a listener.
    this.callee.on('TEST\_CALL', (data: rpc.MessageSequence) => {
      let recv = new TestParcelable();
      data.readParcelable(recv);
      recv.age++;
      return recv;
    });
  }

  onDestroy(): void {
    hilog.info(DOMAIN, LOG\_TAG, '%{public}s', 'Ability onDestroy');
    // Unregisters the listener.
    this.callee.off('TEST\_CALL');
  }
}

The following code demonstrates the scenario where the caller launches the callee to the foreground.

import { Caller, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const LOG\_TAG = 'TEST\_TAG';

export default class EntryAbility extends UIAbility {
  async onForeground() {
    let caller: Caller;
    // Launch the UIAbility to the foreground and set 'ohos.aafwk.param.callAbilityToForeground' in parameters to true.
    let wantForeground: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      parameters: {
        'ohos.aafwk.param.callAbilityToForeground': true
      }
    };

    try {
      caller = await this.context.startAbilityByCall(wantForeground);
      caller.release();
    } catch (err) {
      // Process input parameter errors.
      hilog.error(DOMAIN, LOG\_TAG, \`startAbilityByCall failed ${err}\`);
    }
  }
}

#### \[h2\]setMissionLabel

setMissionLabel(label: string, callback: AsyncCallback<void>): void

Sets a mission label for this UIAbility on the multitasking screen. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| label | string | Yes | Mission label. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.setMissionLabel('test', (result: BusinessError) => {
      console.info(\`setMissionLabel: ${JSON.stringify(result)}\`);
    });
  }
}

#### \[h2\]setMissionLabel

setMissionLabel(label: string): Promise<void>

Sets a mission label for this UIAbility on the multitasking screen. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| label | string | Yes | Mission label. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.setMissionLabel('test').then(() => {
      console.info('success');
    }).catch((err: BusinessError) => {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`setMissionLabel failed, code is ${code}, message is ${message}\`);
    });
  }
}

#### \[h2\]setMissionContinueState10+

setMissionContinueState(state: AbilityConstant.ContinueState, callback: AsyncCallback<void>): void

Sets the mission continuation state of this UIAbility. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AbilityConstant.ContinueState](../../../stage-model/ohos-app-ability-abilityconstant-ability-related-constants/document.md#continuestate10) | Yes | Mission continuation state. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result: BusinessError) => {
      console.info(\`setMissionContinueState: ${JSON.stringify(result)}\`);
    });
  }
}

#### \[h2\]setMissionContinueState10+

setMissionContinueState(state: AbilityConstant.ContinueState): Promise<void>

Sets the mission continuation state of this UIAbility. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [AbilityConstant.ContinueState](../../../stage-model/ohos-app-ability-abilityconstant-ability-related-constants/document.md#continuestate10) | Yes | Mission continuation state. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE).then(() => {
      console.info('success');
    }).catch((err: BusinessError) => {
      console.error(\`setMissionContinueState failed, code is ${err.code}, message is ${err.message}\`);
    });
  }
}

#### \[h2\]restoreWindowStage

restoreWindowStage(localStorage: LocalStorage): void

Restores the WindowStage data in the UIAbility. It can be called only on the main thread.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localStorage | LocalStorage | Yes | Storage used to store the restored window stage. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let storage = new LocalStorage();
    this.context.restoreWindowStage(storage);
  }
}

#### \[h2\]isTerminating

isTerminating(): boolean

Checks whether this UIAbility is in the terminating state.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the UIAbility is in the terminating state. **true** if in the terminating state, **false** otherwise. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000011 | The context does not exist. |

**Example**

import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let isTerminating: boolean = this.context.isTerminating();
    console.info(\`ability state is ${isTerminating}\`);
  }
}

#### \[h2\]requestDialogService

requestDialogService(want: Want, result: AsyncCallback<dialogRequest.RequestResult>): void

Starts a ServiceExtensionAbility that supports modal dialog boxes. After the ServiceExtensionAbility is started, the application displays a modal dialog box. You can call [setRequestResult](../../../both-models-recommended/ohos-app-ability-dialogrequest-dialogrequest-module/document.md#requestcallbacksetrequestresult) to obtain the result. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/EOofCdE_R5GTyY6dku61wA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=942102A9CA1FF589FD3D25D0F87B1EA9403C7A665AA60E83EB6030CB90AD89BE)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information for starting the ServiceExtensionAbility. |
| result | AsyncCallback<[dialogRequest.RequestResult](../../../both-models-recommended/ohos-app-ability-dialogrequest-dialogrequest-module/document.md#requestresult)\> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0** and **data** the result of the request for a modal dialog box. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
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
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want, dialogRequest } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AuthAccountServiceExtension'
    };

    try {
      this.context.requestDialogService(want, (err: BusinessError, result: dialogRequest.RequestResult) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`requestDialogService failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info(\`requestDialogService succeed, result = ${JSON.stringify(result)}\`);
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`requestDialogService failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]requestDialogService

requestDialogService(want: Want): Promise<dialogRequest.RequestResult>

Starts a ServiceExtensionAbility that supports modal dialog boxes. After the ServiceExtensionAbility is started, the application displays a modal dialog box. You can call [setRequestResult](../../../both-models-recommended/ohos-app-ability-dialogrequest-dialogrequest-module/document.md#requestcallbacksetrequestresult) to obtain the result. This API uses a promise to return the result. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/-g23pGE8T3CM7gv880rqjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94D1F15B4908B1BA973787863B589E9359200CC9FA64132EE5EC6DFE60C40B95)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information for starting the ServiceExtensionAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[dialogRequest.RequestResult](../../../both-models-recommended/ohos-app-ability-dialogrequest-dialogrequest-module/document.md#requestresult)\> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
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
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, Want, dialogRequest } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'AuthAccountServiceExtension'
    };

    try {
      this.context.requestDialogService(want)
        .then((result: dialogRequest.RequestResult) => {
          // Carry out normal service processing.
          console.info(\`requestDialogService succeed, result = ${JSON.stringify(result)}\`);
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(\`requestDialogService failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`requestDialogService failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]reportDrawnCompleted10+

reportDrawnCompleted(callback: AsyncCallback<void>): void

Called when the window content associated with the UIAbility finishes drawing. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **code** in **err** is **0**. Otherwise, **err** contains the corresponding error code and error information. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        return;
      }

      try {
        this.context.reportDrawnCompleted((err) => {
          if (err.code) {
            // Process service logic errors.
            console.error(\`reportDrawnCompleted failed, code is ${err.code}, message is ${err.message}\`);
            return;
          }
          // Carry out normal service processing.
          console.info('reportDrawnCompleted succeed');
        });
      } catch (err) {
        // Capture the synchronization parameter error.
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(\`reportDrawnCompleted failed, code is ${code}, message is ${message}\`);
      }
    });
    console.info("MainAbility onWindowStageCreate");
  }
};

#### \[h2\]startAbilityByType11+

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>) : void

Implicitly starts a given type of [UIExtensionAbility](../../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md). This API uses an asynchronous callback to return the result. It can be called only in the main thread and by applications running in the foreground.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the UIExtensionAbility to start. For details, see [Starting an Application of the Specified Type](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/start-intent-panel#matching-rules). |
| wantParam | Record<string, Object> | Yes | Extended parameter. |
| abilityStartCallback | [AbilityStartCallback](../abilitystartcallback/document.md) | Yes | Callback used to return the detailed error information if the startup fails. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, common } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let wantParam: Record<string, Object> = {
      'time': '2023-10-23 20:45'
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.info(\`code:\` + code + \`name:\` + name + \`message:\` + message);
      },
      onResult: (abilityResult: common.AbilityResult) => {
        console.info(\`resultCode:\` + abilityResult.resultCode + \`bundleName:\` + abilityResult.want?.bundleName);
      }
    };

    this.context.startAbilityByType("photoEditor", wantParam, abilityStartCallback, (err) => {
      if (err) {
        console.error(\`startAbilityByType fail, err: ${JSON.stringify(err)}\`);
      } else {
        console.info(\`success\`);
      }
    });
  }
}

#### \[h2\]startAbilityByType11+

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback) : Promise<void>

Implicitly starts a given type of [UIExtensionAbility](../../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md). This API uses a promise to return the result. It can be called only in the main thread and by applications running in the foreground.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the UIExtensionAbility to start. For details, see [Starting an Application of the Specified Type](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/start-intent-panel#matching-rules). |
| wantParam | Record<string, Object> | Yes | Extended parameter. |
| abilityStartCallback | [AbilityStartCallback](../abilitystartcallback/document.md) | Yes | Callback used to return the detailed error information if the startup fails. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

**Example**

import { UIAbility, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let wantParam: Record<string, Object> = {
      'time': '2023-10-23 20:45'
    };
    let abilityStartCallback: common.AbilityStartCallback = {
      onError: (code: number, name: string, message: string) => {
        console.info(\`code:\` + code + \`name:\` + name + \`message:\` + message);
      },
      onResult: (abilityResult: common.AbilityResult) => {
        console.info(\`resultCode:\` + abilityResult.resultCode + \`bundleName:\` + abilityResult.want?.bundleName);
      }
    };

    this.context.startAbilityByType("photoEditor", wantParam, abilityStartCallback).then(() => {
      console.info(\`startAbilityByType success\`);
    }).catch((err: BusinessError) => {
      console.error(\`startAbilityByType fail, err: ${JSON.stringify(err)}\`);
    });
  }
}

#### \[h2\]showAbility12+

showAbility(): Promise<void>

Shows this UIAbility. This API uses a promise to return the result. It can be called only on the main thread.

Before calling this API, ensure that the application has been added to the status bar.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PC/2-in-1 devices and tablets. On other devices, it returns the error code 801.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not support. |
| 16000050 | Internal error. |
| 16000067 | The StartOptions check failed. |

**Example**

// Index.ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State showAbility: string = 'showAbility'

  build() {
    Row() {
      Column() {
        Text(this.showAbility)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

            context.showAbility().then(() => {
              console.info(\`showAbility success\`);
            }).catch((err: BusinessError) => {
              console.error(\`showAbility fail, err: ${JSON.stringify(err)}\`);
            });
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}

// EntryAbility.ts
import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
      processMode: contextConstant.ProcessMode.NEW\_PROCESS\_ATTACH\_TO\_STATUS\_BAR\_ITEM,
      startupVisibility: contextConstant.StartupVisibility.STARTUP\_SHOW
    };

    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbility succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]hideAbility12+

hideAbility(): Promise<void>

Hides this UIAbility. This API uses a promise to return the result. It can be called only on the main thread.

Before calling this API, ensure that the application has been added to the status bar.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PC/2-in-1 devices and tablets. On other devices, it returns the error code 801.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not support. |
| 16000050 | Internal error. |
| 16000067 | The StartOptions check failed. |

**Example**

// Index.ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State hideAbility: string = 'hideAbility'

  build() {
    Row() {
      Column() {
        Text(this.hideAbility)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

            context.hideAbility().then(() => {
              console.info(\`hideAbility success\`);
            }).catch((err: BusinessError) => {
              console.error(\`hideAbility fail, err: ${JSON.stringify(err)}\`);
            });
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}

// EntryAbility.ts
import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
      processMode: contextConstant.ProcessMode.NEW\_PROCESS\_ATTACH\_TO\_STATUS\_BAR\_ITEM,
      startupVisibility: contextConstant.StartupVisibility.STARTUP\_HIDE
    };

    try {
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // Process service logic errors.
          console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
          return;
        }
        // Carry out normal service processing.
        console.info('startAbility succeed');
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]moveAbilityToBackground12+

moveAbilityToBackground(): Promise<void>

Moves this UIAbility from the foreground to the background. This API uses a promise to return the result. It can be called only on the main thread.

This API can be used only on phones.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**

-   Starting from API version 12, this API can be properly called on phones, wearables, and TVs. If it is called on other device types, error code 16000061 is returned.
-   Starting from API version 13, this API can be properly called on phones, tablets, wearables, and TVs. If it is called on other device types, error code 16000061 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000061 | Operation not supported. |
| 16000065 | The API can be called only when the ability is running in the foreground. |
| 16000066 | An ability cannot switch to the foreground or background in Wukong mode. |

**Example**

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State moveAbilityToBackground: string = 'Move To Background'

  build() {
    Row() {
      Column() {
        Text(this.moveAbilityToBackground)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

            context.moveAbilityToBackground().then(() => {
              console.info(\`moveAbilityToBackground success.\`);
            }).catch((err: BusinessError) => {
              console.info(\`moveAbilityToBackground error: ${JSON.stringify(err)}.\`);
            });
          });
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]openAtomicService12+

openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>

Opens an atomic service in an independent window. This API uses a promise to return the result. It can be called only on the main thread.

After an atomic service is started, the following situations may occur:

-   Normally, the atomic service can call [terminateSelfWithResult](#terminateselfwithresult) to terminate itself. The result is returned to the caller.
-   If an exception occurs, for example, the atomic service is killed, an exception result, in which **resultCode** is **\-1**, is returned to the caller.
-   If the atomic service is started multiple times by different applications calling this API, when the atomic service calls [terminateSelfWithResult](#terminateselfwithresult) to terminate itself, it will only return the normal result to the last caller. All other callers will receive an exception result with **resultCode** set to **\-1**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Gkm9KCHJQ_iqPlq4m-F8dQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8C2B8F42C87EC9E923C2D1B2D913F5AC62CBBCA7706A9D3AE2F23F66C9DAD76)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Unique ID of the application, which is allocated by the cloud. |
| options | [AtomicServiceOptions](../../../stage-model/ohos-app-ability-atomicserviceoptions-optional-parameters-of-openatomicservice/document.md) | No | Parameter carried in the request for starting the atomic service. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityResult](../../ability/abilityresult/document.md)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000002 | Incorrect ability type. |
| 16000003 | The specified ID does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**Example**

import { UIAbility, common, AtomicServiceOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let appId: string = '6918661953712445909';
    let options: AtomicServiceOptions = {
      displayId: 0
    };

    try {
      this.context.openAtomicService(appId, options)
        .then((result: common.AbilityResult) => {
          // Carry out normal service processing.
          console.info('openAtomicService succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(\`openAtomicService failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`openAtomicService failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]openLink12+

openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>

Starts a UIAbility by using [App Linking](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup) or [Deep Linking](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/deep-linking-startup), and returns the exit result of the launched UIAbility via a callback. This API uses a promise to return the result. It can be called only on the main thread.

A URL in the standard format is passed in to the **link** field to start the target UIAbility based on the implicit Want matching rules. The target UIAbility must have the following filter characteristics to process links of App Linking:

-   The **actions** field must contain **ohos.want.action.viewData**.
-   The **entities** field must contain **entity.system.browsable**.
-   The **uris** field must contain elements whose **scheme** is **https** and **domainVerify** is **true**.

If you want to obtain the result after the started UIAbility is terminated, set the **callback** parameter. For details about how to use this parameter, see [startAbilityForResult](#startabilityforresult).

If an input parameter is invalid, for example, a mandatory parameter is not set or the URL set in **link** is not in the standard format, an exception is thrown. If the parameter verification is successful but an error occurs when starting the target UIAbility, the error information is returned through promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/hsMiB8HOTSKlu-IxJZPfrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10F123AF6158E1751C50068389BEECFA75F6FCB878C14B5115F67712F55F324E)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| link | string | Yes | URL to open, which must be in the standard format. |
| options | [OpenLinkOptions](../../../stage-model/ohos-app-ability-openlinkoptions-optional-parameters-of-openlink/document.md) | No | Options of the URL. |
| callback | AsyncCallback<[AbilityResult](../../ability/abilityresult/document.md)\> | No | Callback used to return the result. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
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
| 16200001 | The caller has been released. |
| 16000053 | The ability is not on the top of the UI. |

**Example**

import { common, OpenLinkOptions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0xeeee;
const TAG: string = '\[openLinkDemo\]';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("Call StartAbilityForResult")
        .onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let link: string = 'https://www.example.com';
          let openLinkOptions: OpenLinkOptions = {
            appLinkingOnly: true,
            parameters: { demo\_key: 'demo\_value' }
          };

          try {
            context.openLink(
              link,
              openLinkOptions,
              (err, result) => {
                hilog.error(DOMAIN, TAG, \`openLink callback error.code: ${JSON.stringify(err)}\`);
                hilog.info(DOMAIN, TAG, \`openLink callback result: ${JSON.stringify(result.resultCode)}\`);
                hilog.info(DOMAIN, TAG, \`openLink callback result data: ${JSON.stringify(result.want)}\`);
              }
            ).then(() => {
              hilog.info(DOMAIN, TAG, \`open link success.\`);
            }).catch((err: BusinessError) => {
              hilog.error(DOMAIN, TAG, \`open link failed, errCode ${JSON.stringify(err.code)}\`);
            });
          }
          catch (e) {
            hilog.error(DOMAIN, TAG, \`exception occured, errCode ${JSON.stringify(e.code)}\`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### \[h2\]backToCallerAbilityWithResult12+

backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>

Returns the startup result to the caller of [startAbilityForResult](#startabilityforresult) or [openLink](#openlink12). Different from [terminateSelfWithResult](#terminateselfwithresult), this API does not destroy the current UIAbility when it returns the result. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityResult | [AbilityResult](../../ability/abilityresult/document.md) | Yes | Result returned to the caller. |
| requestCode | string | Yes | Request code generated by the system when the target UIAbility is started using [startAbilityForResult](#startabilityforresult) or [openLink](#openlink12). The value can be obtained from the [CALLER\_REQUEST\_CODE](../../../both-models-recommended/ohos-app-ability-wantconstant-want-constants/document.md) field in **want**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000074 | The caller does not exist. |
| 16000075 | BackToCaller is not supported. |

**Example**

The caller uses **startAbilityForResult** to start a UIAbility, and the target UIAbility calls **backToCallerAbilityWithResult** to return the result to the caller.

// Caller
// index.ets
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)

        Button("Call StartAbilityForResult")
          .onClick(() => {
            let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let want: Want = {
              bundleName: 'com.example.demo2',
              abilityName: 'EntryAbility'
            };

            try {
              // Use startAbilityForResult to start the target UIAbility.
              context.startAbilityForResult(want, (err: BusinessError, result: common.AbilityResult) => {
                if (err.code) {
                  // Process service logic errors.
                  hilog.error(0x0000, 'testTag', \`startAbilityForResult failed, code is ${err.code}, message is ${err.message}\`);
                  this.message = \`startAbilityForResult failed: code is ${err.code}, message is ${err.message}\`
                  return;
                }
                // Carry out normal service processing.
                hilog.info(0x0000, 'testTag', \`startAbilityForResult succeed\`);
                hilog.info(0x0000, 'testTag', \`AbilityResult is ${JSON.stringify(result)}\`);
                this.message = \`AbilityResult.resultCode: ${JSON.stringify(result.resultCode)}\`
              });
            } catch (err) {
              // Process input parameter errors.
              let code = (err as BusinessError).code;
              let message = (err as BusinessError).message;
              hilog.error(0x0000, 'testTag', \`startAbilityForResult failed, code is ${code}, message is ${message}\`);
              this.message = \`startAbilityForResult failed, code is ${code}, message is ${message}\`;
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

// Target UIAbility
// EntryAbility.ets
import { AbilityConstant, common, UIAbility, Want, wantConstant } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // Obtain the CALLER\_REQUEST\_CODE of the caller from want and save it.
    let callerRequestCode: string = want?.parameters?.\[wantConstant.Params.CALLER\_REQUEST\_CODE\] as string;
    AppStorage.setOrCreate<string>("callerRequestCode", callerRequestCode)
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let callerRequestCode: string = want?.parameters?.\[wantConstant.Params.CALLER\_REQUEST\_CODE\] as string;
    AppStorage.setOrCreate<string>("callerRequestCode", callerRequestCode)
  }

  onForeground(): void {
    // Obtain the saved CALLER\_REQUEST\_CODE.
    let callerRequestCode: string = AppStorage.get<string>("callerRequestCode") as string;
    hilog.info(0x0000, 'testTag', \`callerRequestCode is ${callerRequestCode}\`);
    let want: Want = {};
    let resultCode = 100;
    let abilityResult: common.AbilityResult = {
      want,
      resultCode
    };
    try {
      // Return the result to the caller.
      this.context.backToCallerAbilityWithResult(abilityResult, callerRequestCode)
        .then(() => {
          // Carry out normal service processing.
          hilog.info(0x0000, 'testTag', 'backToCallerAbilityWithResult succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          hilog.error(0x0000, 'testTag', \`backToCallerAbilityWithResult failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Capture the synchronization parameter error.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(0x0000, 'testTag', \`backToCallerAbilityWithResult failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]setRestoreEnabled14+

setRestoreEnabled(enabled: boolean): void

Sets whether to enable backup and restore for this UIAbility.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable backup and restore. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 16000011 | The context does not exist. |

**Example**

import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let enabled = true;
    try {
      this.context.setRestoreEnabled(enabled);
    } catch (paramError) {
      let code = (paramError as BusinessError).code;
      let message = (paramError as BusinessError).message;
      console.error(\`setRestoreEnabled failed, err code: ${code}, err msg: ${message}\`);
    }
  }
}

#### \[h2\]startUIServiceExtensionAbility14+

startUIServiceExtensionAbility(want: Want): Promise<void>

Starts a UIServiceExtensionAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/MLxrqDIbTbeeWezhblC0Rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C735ED980A1255ADB584EED714C282EE58E15270A72C17D7D8B8D9F6849702C)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIServiceExtensionAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**Example**

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        // Create a Start button.
        Button('start ability')
          .enabled(true)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let startWant: Want = {
              bundleName: 'com.acts.uiserviceextensionability',
              abilityName: 'UiServiceExtAbility',
            };
            try {
              // Start the UIServiceExtensionAbility.
              context.startUIServiceExtensionAbility(startWant).then(() => {
                console.info('startUIServiceExtensionAbility success');
              }).catch((error: BusinessError) => {
                console.info('startUIServiceExtensionAbility error', JSON.stringify(error));
              })
            } catch (err) {
              console.info('startUIServiceExtensionAbility failed', JSON.stringify(err));
            }
          })
      }
    }
  }
}

#### \[h2\]connectUIServiceExtensionAbility14+

connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

Connects to a UIServiceExtensionAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/4Cjord0zQYGR-LayoDIdDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=202F3021905D0848B61836EF6535491A311E5A345CF49EA0B538DF21C437C5B8)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for connecting to the UIServiceExtensionAbility. |
| callback | [UIServiceExtensionConnectCallback](../uiserviceextensionconnectcallback/document.md) | Yes | Callback for connecting to the UIServiceExtensionAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<UIServiceProxy> | Promise used to return the result, which is a [UIServiceProxy](../uiserviceproxy/document.md) object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 801 | Capability not supported. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000055 | Installation-free timed out. |

**Example**

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '\[Extension\] ';

@Entry
@Component
struct UIServiceExtensionAbility {
  dataCallBack : common.UIServiceExtensionConnectCallback = {
    // Receive data
    onData: (data: Record<string, Object>) => {
      console.info(\`dataCallBack received data\`, JSON.stringify(data));
    },
    // Disconnect from the UIServiceExtensionAbility.
    onDisconnect: () => {
      console.info(\`dataCallBack onDisconnect\`);
    }
  }

  async myConnect() {
    // Obtain the context.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let startWant: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'UiServiceExtAbility'
    };

    try {
      // Connect to the UIServiceExtensionAbility.
      context.connectUIServiceExtensionAbility(startWant, this.dataCallBack)
        .then((proxy: common.UIServiceProxy) => {
          console.info(TAG + \`try to connectUIServiceExtensionAbility\`, JSON.stringify(proxy));
        }).catch((err: Error) => {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.info(TAG + \`connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.info(TAG + \`connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    };
  }

  build() {
    RelativeContainer() {
      // Create a Connect button.
      Button('connectServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.myConnect()
        });
    }
    .height('100%')
    .width('100%')
  }
}

#### \[h2\]disconnectUIServiceExtensionAbility14+

disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>

Disconnects from a UIServiceExtensionAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/EA0YaMTEQrK3DiXrmF4g9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73F8019ABCAAED190D91B51EC5994B794E07298F34DCA580D372E6B296BCA6C0)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| proxy | [UIServiceProxy](../uiserviceproxy/document.md) | Yes | Proxy returned after [connectUIServiceExtensionAbility](#connectuiserviceextensionability14) is called. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '\[Extension\] ';

@Entry
@Component
struct UIServiceExtensionAbility {
  comProxy: common.UIServiceProxy | null = null;

  build() {
    Scroll() {
      Column() {
        // Create a Disconnect button.
        Button('disconnectUIServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
          .margin({
            top: 5,
            left: 10,
            right: 10,
            bottom: 5
          })
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.myDisconnectUIServiceExtensionAbility()
          });
      }
      .width('100%')
    }
    .height('100%')
  }

  myDisconnectUIServiceExtensionAbility() {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    try {
      // Disconnect from the UIServiceExtensionAbility.
      context.disconnectUIServiceExtensionAbility(this.comProxy)
        .then(() => {
          console.info(TAG + \`disconnectUIServiceExtensionAbility succeed ${this.comProxy}\`);
        }).catch((err: Error) => {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.info(TAG + \`disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.info(TAG + \`disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]setAbilityInstanceInfo15+

setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>

Sets the icon and label for this UIAbility. The icon and label can be displayed in the task center and the shortcut bar. This API uses a promise to return the result.

**Required permissions**: ohos.permission.SET\_ABILITY\_INSTANCE\_INFO

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| label | string | Yes | New icon label. The label cannot be an empty string, and can contain a maximum of 1024 bytes. |
| icon | [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Icon. The recommended icon size is 512 px \* 512 px. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', async (err, data) => {
      if (err.code) {
        console.error(\`loadContent failed, code is ${err.code}\`);
        return;
      }

      let newLabel: string = 'instance label';
      let color = new ArrayBuffer(512 \* 512 \* 4); // Create an ArrayBuffer object to store image pixels. The size of the object is (height \* width \* 4) bytes.
      let bufferArr = new Uint8Array(color);
      for (let i = 0; i < bufferArr.length; i += 4) {
        bufferArr\[i\] = 255;
        bufferArr\[i+1\] = 0;
        bufferArr\[i+2\] = 122;
        bufferArr\[i+3\] = 255;
      }
      let opts: image.InitializationOptions = {
        editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 512, width: 512 }
      };
      let imagePixelMap: image.PixelMap = await image.createPixelMap(color, opts);
      this.context.setAbilityInstanceInfo(newLabel, imagePixelMap)
        .then(() => {
          console.info('setAbilityInstanceInfo success');
        }).catch((err: BusinessError) => {
        console.error(\`setAbilityInstanceInfo failed, code is ${err.code}, message is ${err.message}\`);
      });
    });
  }
}

#### \[h2\]revokeDelegator17+

revokeDelegator(): Promise<void>

When the first UIAbility launched under a module needs to redirect to another UIAbility, the target UIAbility is known as the DelegatorAbility. For details about how to set up the DelegatorAbility, see step 1 in the example provided for this API.

Once the DelegatorAbility has completed its specific operations, you can use this API to revert to the first UIAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/FKeHodmiS2mI3qMYSfBsiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47C70C049A5FB2A76F1538E3689B58C872A8E145A599C4A2A5D65DE5EE64A1CA)

After the API is successfully called, the [Window](../../../../../arkui/arkts-api/window-manager/ohos-window-window/module-description/document.md) API within the DelegatorAbility becomes invalid.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not support. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000065 | The API can be called only when the ability is running in the foreground. |
| 16000084 | Only DelegatorAbility is allowed to call this API, and only once. |
| 16000085 | An error occurred during the interaction between the ability and window. |

**Example**

1.  Set a DelegatorAbility.
    
    Configure **abilitySrcEntryDelegator** and **abilityStageSrcEntryDelegator** in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file. When the first UIAbility of the module is cold started, the system preferentially starts the UIAbility specified by **abilitySrcEntryDelegator**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/CvIwKUlfRyKI0a_Rs265NA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95DD53E468071ACD591F58D9DCE9878949EC281969CCC29C5132F6F52219FCC2)
    
    -   If the UIAbility is started by calling [startAbilityByCall](#startabilitybycall), the system ignores **abilitySrcEntryDelegator** and **abilityStageSrcEntryDelegator** configured in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file.
    -   The module name specified by **abilityStageSrcEntryDelegator** must be different from the current module name.
    
    {
      "module": {
        // ...
        "abilityStageSrcEntryDelegator": "xxxModuleName",
        "abilitySrcEntryDelegator": "xxxAbilityName",
        // ...
      }
    }
    
2.  Revoke the DelegatorAbility.
    
    import { UIAbility } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    export default class DelegatorAbility extends UIAbility {
      onForeground() {
        // After the DelegatorAbility completes the specific operation, call revokeDelegator to revert to the first UIAbility.
        this.context.revokeDelegator().then(() => {
          console.info('revokeDelegator success');
        }).catch((err: BusinessError) => {
          console.error(\`revokeDelegator failed, code is ${err.code}, message is ${err.message}\`);
        });
      }
    }
    

#### \[h2\]setColorMode18+

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

Sets the dark/light color mode for this UIAbility. Before calling this API, ensure that the page corresponding to the UIAbility has been loaded. This API can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/_BYCn2agSXad9Dk-32cbVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDE4D0DAF54E45F26DC521247103E45402640F447BD24E654BB6FA803CAF50C1)

-   Before calling this API, ensure that the window has been created and the page corresponding to the UIAbility has been loaded (using the [loadContent](../../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) API in the [onWindowStageCreate()](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onwindowstagecreate) lifecycle).
-   After this API is called, a new resource manager object is created. If a resource manager was previously cached, it should be updated accordingly.
-   The priority of the dark/light color mode is as follows: UIAbility dark/light color mode > Application dark/light color mode (set via [ApplicationContext.setColorMode](../applicationcontext-application-context/document.md#applicationcontextsetcolormode11)) > System dark/light color mode.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorMode | [ConfigurationConstant.ColorMode](../../../both-models-recommended/ohos-app-ability-configurationconstant-constants-related-to-environment-variable/document.md) | Yes | 
Color mode. The options are as follows:

\- **COLOR\_MODE\_DARK**: dark mode.

\- **COLOR\_MODE\_LIGHT**: light mode.

\- **COLOR\_MODE\_NOT\_SET**: not set (following the system or application).

 |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000011 | The context does not exist. |

**Example**

import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content.');
        return;
      }
      let uiAbilityContext = this.context;
      uiAbilityContext.setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_DARK);
    });
  }
}

#### \[h2\]startAppServiceExtensionAbility20+

startAppServiceExtensionAbility(want: Want): Promise<void>

Starts an [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md) instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/EYvVUeuJQ2CkdQRT87MR1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39173FC2D76EBBC6AAB49C7B39C3A598B680AB1C66DAF2B9EE486E6D83E3AE29)

The caller of this API must be the application to which the [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md) instance belongs or an application in the application list supported by the AppServiceExtensionAbility instance (configured in the **appIdentifierAllowList** property of [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities)).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information for starting the [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000200 | The caller is not in the appIdentifierAllowList of the target application. |

**Example**

import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AppServiceExtensionAbility'
    };

    try {
      this.context.startAppServiceExtensionAbility(want)
        .then(() => {
          // Carry out normal service processing.
          console.info('startAppServiceExtensionAbility succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(\`startAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startAppServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]stopAppServiceExtensionAbility20+

stopAppServiceExtensionAbility(want: Want): Promise<void>

Stops an [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md) instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/yyqXPHhyR0-jHdLuVyXzrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF99D1ED4A8A892B9D04C152BE443CE7C7809B18FAA1BB5D81C6B6003E41E35D)

The caller of this API must be the application to which the [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md) instance belongs or an application in the application list supported by the AppServiceExtensionAbility instance (configured in the **appIdentifierAllowList** property of [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities)).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information for stoping the [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000200 | The caller is not in the appIdentifierAllowList of the target application. |

**Example**

import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AppServiceExtensionAbility'
    };

    try {
      this.context.stopAppServiceExtensionAbility(want)
        .then(() => {
          // Carry out normal service processing.
          console.info('stopAppServiceExtensionAbility succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(\`stopAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}\`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`stopAppServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]connectAppServiceExtensionAbility20+

connectAppServiceExtensionAbility(want: Want, callback: ConnectOptions): number

Connects this UIAbility to an [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md). It enables communication with the AppServiceExtensionAbility via a proxy, allowing access to the capabilities exposed by the AppServiceExtensionAbility. It can be called only on the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/PyHg01e3S6Sw4oCYr6tKqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D749C027C99CA510D52040E2117A0565C758796B1919B4072B6A6B201CD7C465)

If the [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md) instance is not started, the caller of this API must be the application to which the [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md) instance belongs or an application in the application list supported by the AppServiceExtensionAbility instance (configured in the **appIdentifierAllowList** property of [extensionAbilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#extensionabilities)).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information for connecting to the [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md). |
| callback | [ConnectOptions](../../ability/connectoptions/document.md) | Yes | Callback used to return the information indicating that the connection is successful, failed, or interrupted. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Connection ID. A caller can call [disconnectAppServiceExtensionAbility](#disconnectappserviceextensionability20) with this ID for disconnection. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000201 | The target service has not been started yet. |

**Example**

import { UIAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'AppServiceExtensionAbility'
    };
    let commRemote: rpc.IRemoteObject;
    let callback: common.ConnectOptions = {
      onConnect(elementName, remote) {
        commRemote = remote;
        console.info('onConnect...');
      },
      onDisconnect(elementName) {
        console.info('onDisconnect...');
      },
      onFailed(code) {
        console.info('onFailed...');
      }
    };
    let connection: number;

    try {
      connection = this.context.connectAppServiceExtensionAbility(want, callback);
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`connectAppServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]disconnectAppServiceExtensionAbility20+

disconnectAppServiceExtensionAbility(connection: number): Promise<void>

Disconnects from an [AppServiceExtensionAbility](../../../stage-model/ohos-app-ability-appserviceextensionability-extensionability-for-application-bac/document.md). It can be called only on the main thread. This API uses a promise to return the result.

Once the connection is terminated, you are advised to set the remote object returned when the connection is established to null, so as to prevent communication using the remote object that may become invalid.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | Connection ID returned by [connectAppServiceExtensionAbility](#connectappserviceextensionability20). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    // connection is the return value of connectAppServiceExtensionAbility.
    let connection = 1;
    let commRemote: rpc.IRemoteObject | null;

    try {
      this.context.disconnectAppServiceExtensionAbility(connection).then(() => {
        commRemote = null;
        // Carry out normal service processing.
        console.info('disconnectAppServiceExtensionAbility succeed');
      }).catch((err: BusinessError) => {
        // Process service logic errors.
        console.error(\`disconnectAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}\`);
      });
    } catch (err) {
      commRemote = null;
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`disconnectAppServiceExtensionAbility failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]setOnNewWantSkipScenarios20+

setOnNewWantSkipScenarios(scenarios: number): Promise<void>

Sets whether to trigger the [onNewWant](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#onnewwant) lifecycle callback when a UIAbility is started in a specific scenario. It can be called only on the main thread. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/FN0j0NKsQXOmMrH3dutk9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF25B68C45EE05C3BEA620409A3C74C0702E4614B4C1D96FFE4F13AF6B0D9A52)

This API is usually used within the [onCreate](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md#oncreate) lifecycle callback. You are advised to include all the enumerated values of [Scenarios](../../../stage-model/ohos-app-ability-contextconstant-context-related-constants/document.md#scenarios20) when specifying the **scenarios** parameter. For details, see the sample code below.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scenarios | number | Yes | Scenarios. For details about the available options, see [Scenarios](../../../stage-model/ohos-app-ability-contextconstant-context-related-constants/document.md#scenarios20). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000050 | Internal error. Possible causes: Connection to service failed. |

**Example**

import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let scenarios: number = contextConstant.Scenarios.SCENARIO\_MOVE\_MISSION\_TO\_FRONT |
      contextConstant.Scenarios.SCENARIO\_SHOW\_ABILITY |
      contextConstant.Scenarios.SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT;

    try {
      this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
        // Carry out normal service processing.
        console.info('setOnNewWantSkipScenarios succeed');
      }).catch((err: BusinessError) => {
        // Process service logic errors.
        console.error(\`setOnNewWantSkipScenarios failed, code is ${err.code}, message is ${err.message}\`);
      });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`setOnNewWantSkipScenarios failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]startSelfUIAbilityInCurrentProcess22+

startSelfUIAbilityInCurrentProcess(want: Want, specifiedFlag: string, options?: StartOptions): Promise<void>

Starts the application's own UIAbility within the current process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/-_hgPXSQS6amUQJnRHKr0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A97B3224CB0C902B2E25DEA1FEC93BF3D89E6B4D102120CD8CA7CF4813F89837)

-   The target UIAbility can only be cold-started. If an instance of the target UIAbility has already been launched, the startup fails.
-   The UIAbility instance started through this API runs in the same process as the caller. Other process-related policies for the target UIAbility (such as those specified via the **isolationProcess** or **isolationMode** fields in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file) does not take effect.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Mandatory information for starting the UIAbility. Only [explicit startup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/explicit-implicit-want-mappings#matching-rules-of-explicit-want) is supported. [Implicit startup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/explicit-implicit-want-mappings#matching-rules-of-implicit-want) is not supported. |
| specifiedFlag | string | Yes | 
ID of the UIAbility. This ID must not duplicate that of any already running UIAbility instance; otherwise, an error is returned.

**NOTE**

When this API is used to start a UIAbility instance in [specified](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#specified) mode, the [onAcceptWant](../../../stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md#onacceptwant) callback is not triggered.

 |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | No | Parameters used for starting the UIAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Connect to system service failed. |
| 16000053 | The ability is not on the top of the UI. |
| 16000122 | The target component is blocked by the system module and does not support startup. |
| 16000123 | Implicit startup is not supported. |
| 16000124 | Starting a remote UIAbility is not supported. |
| 16000130 | The UIAbility not belong to caller. |
| 16000131 | The UIAbility is already exist, can not start again. |

**Example**

import { UIAbility, StartOptions, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let accountId = 100;
    let options: StartOptions = {
      displayId: 0
    };
    
    let instanceFlag = 'instance1';

    try {
      this.context.startSelfUIAbilityInCurrentProcess(want, instanceFlag, options);
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(\`startSelfUIAbilityInCurrentProcess failed, code is ${code}, message is ${message}\`);
    }
  }
}

#### \[h2\]restartApp22+

restartApp(want: Want): Promise<void>

Called by a focused UIAbility to restart its own process and launch a specified UIAbility within the same application. This API can be called only on the main thread. This API uses a promise to return the result.

If the target UIAbility is the current one, this action resets the window to its initial state. If it is a different UIAbility, the system navigates to and open a new window for that UIAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/cQTpHeu4StqoObb_SZjyYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=347B422529B39BE4D2BEFF49E635961D1422940802DF39C63189D11489483EBB)

When this API is called to restart the process, the **onDestroy** lifecycle callback of the UIAbility in the process is not triggered.

If an atomic service calls this API, [restartSelfAtomicService()](../../../both-models-recommended/ohos-app-ability-abilitymanager-ability-information-management/document.md#abilitymanagerrestartselfatomicservice20), or [ApplicationContext.restartApp()](../applicationcontext-application-context/document.md#applicationcontextrestartapp12) within 3 seconds after a successful call to this API, the system returns error code 16000064.

If an application calls this API or [ApplicationContext.restartApp()](../applicationcontext-application-context/document.md#applicationcontextrestartapp12) within 3 seconds after a successful call to this API, the system returns error code 16000064.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on phones. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information about the UIAbility to start. The bundle name and ability name are verified. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Connect to system server error. |
| 16000063 | The target to restart does not belong to the caller or is not a UIAbility. |
| 16000064 | Restart too frequently. |
| 16000065 | The API can be called only when the ability is focused. |

**Example**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'restartApp with window';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page\_text\_font\_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(async () => {
          let want: Want = {
            bundleName: 'com.example.myapplication',
            abilityName: 'EntryAbility'
          };
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          try {
            await context.restartApp(want);
          } catch (err) {
            hilog.error(0x0000, 'testTag', \`restart failed: ${err.code}, ${err.message}\`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### \[h2\]setMissionWindowIcon22+

setMissionWindowIcon(windowIcon: image.PixelMap): Promise<void>

Sets the icon for this UIAbility, which is displayed in the application window, application card in the mission center, and window snapshot in the shortcut bar. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/cyw3yq9YSeS7JGLTOf5HkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=700CBC0E13E3E4786DDB67B24A5CD40A3AB362060F588AD5D6DC5F97861E820B)

There is no priority relationship among the **setMissionWindowIcon** and [setAbilityInstanceInfo](#setabilityinstanceinfo15). The icon set by the last called API takes effect. If these APIs are called sequentially, the icon set by the last call takes precedence and overwrites any previous settings.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowIcon | [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Icon of the UIAbility displayed in the application window, application card in the mission center, and window snapshot in the shortcut bar. The icon must be a square and its size must not exceed 128 MB. Otherwise, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |
| 16000050 | Internal error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |
| 16000135 | The main window of this ability not exist. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let imagePixelMap: image.PixelMap;
    let color = new ArrayBuffer(1024 \* 1024 \* 4); // Create an ArrayBuffer object to store image pixels. The size of the object is (height \* width \* 4) bytes.
    let bufferArr = new Uint8Array(color);
    for (let i = 0; i < bufferArr.length; i += 4) {
      bufferArr\[i\] = 255;
      bufferArr\[i+1\] = 0;
      bufferArr\[i+2\] = 122;
      bufferArr\[i+3\] = 255;
    }
    image.createPixelMap(color, {
      editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 1024, width: 1024 }
    }).then((data) => {
      imagePixelMap = data;
      this.context.setMissionWindowIcon(imagePixelMap)
        .then(() => {
          console.info('setMissionWindowIcon succeed');
        })
        .catch((err: BusinessError) => {
          console.error(\`setMissionWindowIcon failed, code is ${err.code}, message is ${err.message}\`);
        });
    }).catch((err: BusinessError) => {
      console.error(\`createPixelMap failed, code is ${err.code}, message is ${err.message}\`);
    });
  }
}
