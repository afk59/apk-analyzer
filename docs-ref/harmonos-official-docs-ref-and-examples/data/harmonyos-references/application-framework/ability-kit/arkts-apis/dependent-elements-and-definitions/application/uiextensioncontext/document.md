# UIExtensionContext

UIExtensionContext provides the context environment for the [UIExtensionAbility](../../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md). It inherits from [ExtensionContext](../extensioncontext/document.md) and provides UIExtensionAbility-related configurations and APIs for operating the [UIAbility](../../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). For example, you can use the APIs to start a UIAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/jsD59n4sRPGX-fpzh3pRvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D065AA8D8E2BFFB84FA0539D04BEC39A1F1D43DF440DC3C61626AE2751EA649F)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.
-   The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

#### Modules to Import

import { common } from '@kit.AbilityKit';

#### UIExtensionContext

#### \[h2\]startAbility

startAbility(want: Want, callback: AsyncCallback<void>): void

Starts a UIAbility. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/sGD_2Qo4QeChuQyXpeWTZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DD03C18767CA6344BD4C8AD82854D8040681937D3149945B86B2BB319C0ABD3)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want required for starting the UIAbility, which contains information such as the name of the UIAbility to start. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the UIAbility is started, **err** is **undefined**; otherwise, **err** is an error object. |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {

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

Starts a UIAbility. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/DaYWOeF9T-CTLDiRQHEaCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=797452569F50CD97EB429ACE5C5D9A09B8CFAAAFABA20DE7E222319F50083DA6)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want required for starting the UIAbility, which contains information such as the name of the UIAbility to start. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | Yes | Extra parameters used for starting the UIAbility. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the UIAbility is started, **err** is **undefined**; otherwise, **err** is an error object. |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

Starts a UIAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/fsGpFyRmQcu6sYq5Z9lzxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE647A70015A3BE1DA2CFC75B6733B447F09355F825CD652F61CA63F9E8FFEDA)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want required for starting the UIAbility, which contains information such as the name of the UIAbility to start. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | No | Extra parameters used for starting the UIAbility. |

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
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
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

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses an asynchronous callback to return the result. The following situations may be possible for a started UIAbility:

-   Normally, you can call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the UIAbility. The result is returned to the caller.
-   If an exception occurs, for example, the UIAbility is killed, an error message, in which **resultCode** is **\-1**, is returned to the initiator UIAbility.
-   If different applications call this API to start a UIAbility that uses the singleton mode and then call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the UIAbility, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **\-1**, is returned to others.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Av88JXyDSKSS9Dpa-k1QGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0381B96F962C6EFD20DF58E3583A9B5F68AF6CA72067F5F70F3F7E992C26C7D)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want required for starting the UIAbility, which contains information such as the name of the UIAbility to start. |
| callback | AsyncCallback<[AbilityResult](../../ability/abilityresult/document.md)\> | Yes | Callback used to return the result. |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
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

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses an asynchronous callback to return the result. The following situations may be possible for a started UIAbility:

-   Normally, you can call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the UIAbility. The result is returned to the caller.
-   If an exception occurs, for example, the UIAbility is killed, an error message, in which **resultCode** is **\-1**, is returned to the initiator UIAbility.
-   If different applications call this API to start a UIAbility that uses the singleton mode and then call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the UIAbility, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **\-1**, is returned to others.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/dF9M6n5WT2ycPYOMI1roqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D0307C07AE9AC2E645D656C398516096F454791240B103F70572BA115637FA5)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want required for starting the UIAbility, which contains information such as the name of the UIAbility to start. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | Yes | Extra parameters used for starting the UIAbility. |
| callback | AsyncCallback<[AbilityResult](../../ability/abilityresult/document.md)\> | Yes | Callback used to return the result. |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
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

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses a promise to return the result. The following situations may be possible for a started UIAbility:

-   Normally, you can call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the UIAbility. The result is returned to the caller.
-   If an exception occurs, for example, the UIAbility is killed, an error message, in which **resultCode** is **\-1**, is returned to the initiator UIAbility.
-   If different applications call this API to start a UIAbility that uses the singleton mode and then call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the UIAbility, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **\-1**, is returned to others.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/CmVA-LyxRhaRryK6aaW6TA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55CA6440B23660BA17253E5A61962D0DDEC34F3A720631545E4A0084813037FF)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want required for starting the UIAbility, which contains information such as the name of the UIAbility to start. |
| options | [StartOptions](../../../stage-model/ohos-app-ability-startoptions-optional-parameters-of-startability/document.md) | No | Extra parameters used for starting the UIAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityResult](../../ability/abilityresult/document.md)\> | Promise used to return the exit result of the launched UIAbility. |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, common, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let want: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0,
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

#### \[h2\]connectServiceExtensionAbility

connectServiceExtensionAbility(want: Want, options: ConnectOptions): number

Connects this UIExtensionAbility to a ServiceExtensionAbility. It enables communication with the ServiceExtensionAbility via a proxy, allowing access to the capabilities exposed by the ServiceExtensionAbility.

ServiceExtensionAbility is a special type of [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/extensionability-overview) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/05KfP--bRU2aeDLMepv1GA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FB517AF58E599FBF61C90E7EBDC4DF686219CAC4ED995F16FC7747EAC7D679E)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information required for connecting to the ServiceExtensionAbility, including the ability name and bundle name. |
| options | [ConnectOptions](../../ability/connectoptions/document.md) | Yes | Callback used to return the information indicating that the connection is successful, failed, or interrupted. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Connection ID. The client can call [disconnectServiceExtensionAbility](#disconnectserviceextensionability) with this ID for disconnection. |

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
| 16000070 | The extension cannot start the service. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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
        console.error(\`onFailed, err code: ${code}.\`);
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

Disconnects from a ServiceExtensionAbility. Once the connection is terminated, set the remote object, which is returned when the connection is established, to null. This API uses a promise to return the result.

ServiceExtensionAbility is a special type of [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/extensionability-overview) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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
      })
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

Disconnects from a ServiceExtensionAbility. Once the connection is terminated, set the remote object, which is returned when the connection is established, to null. This API uses an asynchronous callback to return the result.

ServiceExtensionAbility is a special type of [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/extensionability-overview) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | ID of the connected ServiceExtensionAbility, that is, **connectionId** returned by **connectServiceExtensionAbility**. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the disconnection is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

#### \[h2\]terminateSelf12+

terminateSelf(callback: AsyncCallback<void>): void

Destroys this UIExtensionAbility and closes the corresponding window. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

#### \[h2\]terminateSelf12+

terminateSelf(): Promise<void>

Destroys this UIExtensionAbility and closes the corresponding window. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

#### \[h2\]terminateSelfWithResult12+

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

Destroys this UIExtensionAbility, closes the corresponding window, and returns the result to the caller of the UIExtensionAbility (usually a system service). This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [AbilityResult](../../ability/abilityresult/document.md) | Yes | Information returned to the caller of the UIExtensionAbility. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

#### \[h2\]terminateSelfWithResult12+

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

Destroys this UIExtensionAbility, closes the corresponding window, and returns the result to the caller of the UIExtensionAbility (usually a system service). This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [AbilityResult](../../ability/abilityresult/document.md) | Yes | Information returned to the caller of the UIExtensionAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
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

#### \[h2\]reportDrawnCompleted12+

reportDrawnCompleted(callback: AsyncCallback<void>): void

Called when the window content associated with the UIExtensionAbility finishes drawing. The system uses the information to optimize resource allocation, thereby enhancing the efficiency of application startup and display. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the event is reported, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '\[testTag\] ShareExtAbility';

export default class ShareExtAbility extends ShareExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, \`onSessionCreate, want: ${JSON.stringify(want)}\`);
    let data: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(data);
    session.loadContent('pages/extension', storage);
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
  }
}

#### \[h2\]openAtomicService12+

openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>

Opens an atomic service in an independent window and returns the result. This API uses a promise to return the result.

The following situations may be possible for a started atomic service:

-   Normally, you can call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the atomic service. The result is returned to the caller.
-   If an exception occurs, for example, the atomic service is killed, an error message, in which **resultCode** is **\-1**, is returned to the caller.
-   If different applications call this API to start an atomic service and then call [terminateSelfWithResult](../uiabilitycontext/document.md#terminateselfwithresult) to terminate the atomic service, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **\-1**, is returned to others.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/JBq01D-fTayiTxqx_tiU8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6884CAD8DAEA7CDB208711022267C65390B6DD9EAC93CAFC3C50E18EE13C468E)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| appId | string | Yes | Unique ID of the application, which is allocated by the cloud. |
| options | [AtomicServiceOptions](../../../stage-model/ohos-app-ability-atomicserviceoptions-optional-parameters-of-openatomicservice/document.md) | No | Parameter carried in the request for starting the atomic service. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityResult](../../ability/abilityresult/document.md)\> | Promise used to return the information to the caller. |

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
| 16000069 | The extension cannot start the third party application. |
| 16200001 | The caller has been released. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, common, AtomicServiceOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onForeground() {
    let appId: string = '6918661953712445909';
    let options: AtomicServiceOptions = {
      displayId: 0,
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

Starts a UIAbility by using App Linking or Deep Linking. This API uses a promise to return the result.

A URL in the standard format is passed in to the **link** field to start the target UIAbility based on the implicit Want matching rules. The target UIAbility must have the following filter characteristics to process links of App Linking:

-   The **actions** field must contain **ohos.want.action.viewData**.
-   The **entities** field must contain **entity.system.browsable**.
-   The **uris** field must contain elements whose **scheme** is **https** and **domainVerify** is **true**.

If you want to obtain the result after the started UIAbility is terminated, set the **callback** parameter. For details about how to use this parameter, see [startAbilityForResult](#startabilityforresult).

If an input parameter is invalid, for example, a mandatory parameter is not set or the URL set in **link** is not in the standard format, an exception is thrown. If the parameter verification is successful but an error occurs when starting the target UIAbility, the error information is returned through promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/hIBD7HKaSyW05x32VJtmww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=189E6B269BF7FDA310F48A8E9E087F49133FE2240462E1576378F2D8B5FFCED1)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

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
| Promise<void> | that returns no value. |

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
| 16000069 | The extension cannot start the third party application. |
| 16200001 | The caller has been released. |
| 16000053 | The ability is not on the top of the UI. |

**Example**

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, Want, UIExtensionContentSession, OpenLinkOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class ShareExtAbility extends ShareExtensionAbility {
  onCreate() {
    console.info(\`UIExtAbility onCreate\`);
  }

  onForeground() {
    console.info(\`UIExtAbility onForeground\`);
  }

  onBackground() {
    console.info(\`UIExtAbility onBackground\`);
  }

  onDestroy() {
    console.info(\`UIExtAbility onDestroy\`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(\`UIExtAbility onSessionCreate\`);
    console.info(\`UIExtAbility onSessionCreate, want: ${JSON.stringify(want)}\`);
    let record: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(record);
    session.loadContent('pages/UIExtensionIndex', storage);

    let link: string = 'https://www.example.com';
    let openLinkOptions: OpenLinkOptions = {
      appLinkingOnly: true
    };
    try {
      this.context.openLink(
        link,
        openLinkOptions,
        (err, result) => {
          if (err) {
            console.error(\`openLink callback failed, err code: ${err.code}, err msg: ${err.message}.\`);
            return;
          }
          console.info(\`openLink success, result code: ${result.resultCode} result data: ${result.want}.\`);
        }
      ).then(() => {
        console.info(\`open link success.\`);
      }).catch((err: BusinessError) => {
        console.error(\`open link failed, err code: ${err.code}, err msg: ${err.message}.\`);
      });
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(\`openLink failed, err code: ${code}, err msg: ${msg}.\`);
    }
  }

  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(\`UIExtAbility onSessionDestroy\`);
  }
}

#### \[h2\]startUIServiceExtensionAbility14+

startUIServiceExtensionAbility(want: Want): Promise<void>

Starts a UIServiceExtensionAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/XHXawUq5RCWVE8_QGBxPcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B15EDDA765EFE650AEC291EFFB15F06669BD422EDB8EC994BA34FAE747B01CB)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want for starting the UIServiceExtensionAbility. |

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
            let context = this.getUIContext().getHostContext() as common.UIExtensionContext;
            let startWant: Want = {
              bundleName: 'com.acts.uiserviceextensionability',
              abilityName: 'UiServiceExtAbility',
            };
            try {
              // Start the UIServiceExtensionAbility.
              context.startUIServiceExtensionAbility(startWant).then(() => {
                console.info(\`startUIServiceExtensionAbility success.\`);
              }).catch((error: BusinessError) => {
                console.error(\`startUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.\`);
              })
            } catch (err) {
              let code = (err as BusinessError).code;
              let msg = (err as BusinessError).message;
              console.error(\`startUIServiceExtensionAbility failed, err code: ${code}, err msg: ${msg}.\`);
            }
          })
      }
    }
  }
}

#### \[h2\]connectUIServiceExtensionAbility14+

connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

Connects to a UIServiceExtensionAbility. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/ngbu7qXJSaC_UTLNt0lxUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=647EFD0D1272FB7E2FB1616F1474FE9D6570E6EBBE5F2913B124942C9CD1E4A0)

For details about the startup rules for the components in the stage model, see [Component Startup Rules (Stage Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | Want | Yes | Want information used for connection. |
| callback | [UIServiceExtensionConnectCallback](../uiserviceextensionconnectcallback/document.md) | Yes | Callback for connecting to the UIServiceExtensionAbility. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<UIServiceProxy> | Promise used to return a [UIServiceProxy](../uiserviceproxy/document.md) object when the UIServiceExtensionAbility is connected. This object can be used to send data to the UIServiceExtensionAbility. |

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
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000055 | Installation-free timed out. |

**Example**

import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page\_UIServiceExtensionAbility {
  @State uiServiceProxy: common.UIServiceProxy | null = null;

  build() {
    Column() {
      Row() {
        // ...
      }.onClick(() => {
        const context = this.getUIContext().getHostContext() as common.UIExtensionContext;
        const want: Want = {
          deviceId: '',
          bundleName: 'com.example.myapplication',
          abilityName: ''
        };
        // Define a callback.
        const callback: common.UIServiceExtensionConnectCallback = {
          onData: (data: Record<string, Object>): void => {
            console.info(\`onData, data: ${JSON.stringify(data)}.\`);
          },
          onDisconnect: (): void => {
            console.info(\`onDisconnect\`);
          }
        };
        // Connect to the UIServiceExtensionAbility.
        context.connectUIServiceExtensionAbility(want, callback).then((uiServiceProxy: common.UIServiceProxy) => {
          this.uiServiceProxy = uiServiceProxy;
          console.info(\`connectUIServiceExtensionAbility success\`);
        }).catch((error: BusinessError) => {
          console.error(\`connectUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.\`);
        })
      })
    }
  }
}

#### \[h2\]disconnectUIServiceExtensionAbility14+

disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>

Disconnects from a UIServiceExtensionAbility. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| proxy | [UIServiceProxy](../uiserviceproxy/document.md) | Yes | Proxy used returned by calling [connectUIServiceExtensionAbility](#connectuiserviceextensionability14). |

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

@Entry
@Component
struct Page\_UIServiceExtensionAbility {
  @State uiServiceProxy: common.UIServiceProxy | null = null;

  build() {
    Column() {
      Row() {
        // ...
      }.onClick(() => {
        const context = this.getUIContext().getHostContext() as common.UIExtensionContext;
        // this.uiServiceProxy is the proxy object saved during connection.
        context.disconnectUIServiceExtensionAbility(this.uiServiceProxy).then(() => {
          console.info(\`disconnectUIServiceExtensionAbility success.\`);
        }).catch((error: BusinessError) => {
          console.info(\`disconnectUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.\`);
        })
      })
    }
  }
}

#### \[h2\]setColorMode18+

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

Sets the dark/light color mode for this UIExtensionAbility. Before calling this API, ensure that the page corresponding to the UIExtensionContext has been loaded. This API can be called only by the main thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/895gHNeaSiOkzyYbn-2ZSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062210Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F20F365ABBE965C8E8E574814036B602EA41EEC1113B7B620F7FECAA5474C40C)

-   After this API is called, a new resource manager object is created. If a resource manager was previously cached, it should be updated accordingly.
-   The priority of the dark/light color mode is as follows: UIExtensionAbility dark/light color mode > Application dark/light color mode (set via [ApplicationContext.setColorMode](../applicationcontext-application-context/document.md#applicationcontextsetcolormode11)) > System dark/light color mode.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorMode | [ConfigurationConstant.ColorMode](../../../both-models-recommended/ohos-app-ability-configurationconstant-constants-related-to-environment-variable/document.md#colormode) | Yes | 
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

// The UIExtensionAbility class does not allow direct inheritance by third-party applications. The child class ShareExtensionAbility is used here as an example.
import { ShareExtensionAbility, ConfigurationConstant } from '@kit.AbilityKit';

export default class MyAbility extends ShareExtensionAbility {
  onForeground() {
    let uiExtensionContext = this.context;
    uiExtensionContext.setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_DARK);
  }
}
