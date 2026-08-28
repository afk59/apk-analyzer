# @ohos.ability.featureAbility (FeatureAbility Module)

The FeatureAbility module provides APIs that enable user interaction. You can use the APIs to start or terminate an ability, obtain a dataAbilityHelper object, obtain the window corresponding to the current ability, and connect to or disconnect from a ServiceAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/OD9H7ja8S3Wk6_meeSv-6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2B9360F29F910CEBE563E77DAEE12A2D6EAEF822F3C071E0504AFA85D6115A5)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the FA model.

#### Constraints

The APIs of the FeatureAbility module can be called only by PageAbilities.

#### Modules to Import

import { featureAbility } from '@kit.AbilityKit';

#### featureAbility.startAbility

startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void

Starts an ability. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/FtbCrhaESnitMioeSt6pHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21D8B0352FF2740C495DB72A1119735AE2EC93C26B54DBE335A69394DFEEB5BD)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](../ability/startabilityparameter/document.md) | Yes | Ability to start. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **0**; otherwise, **err** is a non-zero value. |

**Example**

import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbility(
  {
    want:
    {
      action: '',
      entities: \[''\],
      type: '',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /\* In the FA model, abilityName consists of package and ability names. \*/
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(\`startAbility fail, error: ${JSON.stringify(error)}\`);
    } else {
      console.info(\`startAbility success, data: ${JSON.stringify(data)}\`);
    }
  }
);

#### featureAbility.startAbility

startAbility(parameter: StartAbilityParameter): Promise<number>

Starts an ability. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Bx3oDr-ASUuxlwMHiu1PdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FB36CDA395D6F1A86A630C8906A2D3962B73A923353138762351C465507A251)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Model restriction**: This API can be used only in the FA model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](../ability/startabilityparameter/document.md) | Yes | Ability to start. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, **0** is returned; otherwise, a non-zero value is returned. |

**Example**

import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: \['entity.system.home'\],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /\* In the FA model, abilityName consists of package and ability names. \*/
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  }
).then((data) => {
  console.info(\`startAbility data: ${JSON.stringify(data)}\`);
});

#### featureAbility.acquireDataAbilityHelper7+

acquireDataAbilityHelper(uri: string): DataAbilityHelper

Obtains a dataAbilityHelper object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/iE2PXKOOS5eCb__U4Thlvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=616A262062A9F25410734AA78D3D51E521F08599D0E4F6B6D781766FC5ECF693)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

To access a DataAbility of another application, the target application must be configured with associated startup (**AssociateWakeUp** set to **true**).

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to open. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataAbilityHelper](../../dependent-elements-and-definitions/ability/dataabilityhelper/document.md) | A utility class used to help other abilities access the Data ability. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

let dataAbilityHelper = featureAbility.acquireDataAbilityHelper(
  'dataability:///com.example.DataAbility'
);

#### featureAbility.startAbilityForResult7+

startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>): void

Starts an ability. This API uses an asynchronous callback to return the result. The following situations may be possible for a started ability:

-   Normally, you can call [terminateSelfWithResult](#featureabilityterminateselfwithresult7) to terminate the ability. The result is returned to the caller.
-   If an exception occurs, for example, the ability is killed, an exception message, in which **resultCode** is **\-1**, is returned to the caller.
-   If different applications call this API to start an ability that uses the singleton mode and then call [terminateSelfWithResult](#featureabilityterminateselfwithresult7) to terminate the ability, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **\-1**, is returned to others.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/4dfGwggQQQWxWPcnyK-zXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DE4BE1468E36A462DDB4E670C5E9BCC9A47B33CEA6F39888CE548B059E84527)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](../ability/startabilityparameter/document.md) | Yes | Ability to start. |
| callback | AsyncCallback<[AbilityResult](../../dependent-elements-and-definitions/ability/abilityresult/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is an AbilityResult object; otherwise, err is an error object. |

**Example**

import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbilityForResult(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: \['entity.system.home'\],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /\* In the FA model, abilityName consists of package and ability names. \*/
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(\`startAbilityForResult fail, error: ${JSON.stringify(error)}\`);
    } else {
      console.info(\`startAbilityForResult success, data: ${JSON.stringify(data)}\`);
    }
  }
);

#### featureAbility.startAbilityForResult7+

startAbilityForResult(parameter: StartAbilityParameter): Promise<AbilityResult>

Starts an ability. This API uses a promise to return the result. The following situations may be possible for a started ability:

-   Normally, you can call [terminateSelfWithResult](#featureabilityterminateselfwithresult7) to terminate the ability. The result is returned to the caller.
-   If an exception occurs, for example, the ability is killed, an exception message, in which **resultCode** is **\-1**, is returned to the caller.
-   If different applications call this API to start an ability that uses the singleton mode and then call [terminateSelfWithResult](#featureabilityterminateselfwithresult7) to terminate the ability, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **\-1**, is returned to others.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/hEjAnvLBTMK3lkMdQ2uVaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=190190E037172CB5A59032A4722455C9AE0626E7628161ECCEC47FC71E9FEDF5)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [StartAbilityParameter](../ability/startabilityparameter/document.md) | Yes | Ability to start. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AbilityResult](../../dependent-elements-and-definitions/ability/abilityresult/document.md)\> | Promise used to return the result. |

**Example**

import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbilityForResult(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: \['entity.system.home'\],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /\* In the FA model, abilityName consists of package and ability names. \*/
      abilityName: 'com.example.myapplication.secondAbility',
      uri: '',
      parameters:
      {
        mykey0: 1111,
        mykey1: \[1, 2, 3\],
        mykey2: '\[1, 2, 3\]',
        mykey3: 'xxxxxxxxxxxxxxxxxxxxxx',
        mykey4: \[1, 15\],
        mykey5: \[false, true, false\],
        mykey6: \['aaaaaa', 'bbbbb', 'ccccccccccc'\],
        mykey7: true,
      },
    },
  },
).then((data) => {
  console.info(\`startAbilityForResult data: ${JSON.stringify(data)}\`);
});

#### featureAbility.terminateSelfWithResult7+

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

Terminates this ability. This API uses an asynchronous callback to return the result. If the ability is started by calling [startAbilityForResult](#featureabilitystartabilityforresult7), the result is returned to the caller when **terminateSelfWithResult** is called. Otherwise, no result is returned to the caller when **terminateSelfWithResult** is called.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [AbilityResult](../../dependent-elements-and-definitions/ability/abilityresult/document.md) | Yes | Result returned after the ability is terminated. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.terminateSelfWithResult(
  {
    resultCode: 1,
    want:
    {
      action: 'ohos.want.action.home',
      entities: \['entity.system.home'\],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /\* In the FA model, abilityName consists of package and ability names. \*/
      abilityName: 'com.example.myapplication.secondAbility',
      uri: '',
      parameters: {
        mykey0: 2222,
        mykey1: \[1, 2, 3\],
        mykey2: '\[1, 2, 3\]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: \[1, 15\],
        mykey5: \[false, true, false\],
        mykey6: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
        mykey7: true,
      }
    },
  },
  (error) => {
    console.error(\`error: ${JSON.stringify(error)}\`);
  }
);

#### featureAbility.terminateSelfWithResult7+

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

Terminates this ability. This API uses a promise to return the result. If the ability is started by calling [startAbilityForResult](#featureabilitystartabilityforresult7), the result is returned to the caller when **terminateSelfWithResult** is called. Otherwise, no result is returned to the caller when **terminateSelfWithResult** is called.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameter | [AbilityResult](../../dependent-elements-and-definitions/ability/abilityresult/document.md) | Yes | Result returned after the ability is terminated. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.terminateSelfWithResult(
  {
    resultCode: 1,
    want:
    {
      action: 'ohos.want.action.home',
      entities: \['entity.system.home'\],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /\* In the FA model, abilityName consists of package and ability names. \*/
      abilityName: 'com.example.myapplication.secondAbility',
      uri:'',
      parameters: {
        mykey0: 2222,
        mykey1: \[1, 2, 3\],
        mykey2: '\[1, 2, 3\]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: \[1, 15\],
        mykey5: \[false, true, false\],
        mykey6: \['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'\],
        mykey7: true,
      }
    },
  }
).then(() => {
  console.info('==========================>terminateSelfWithResult=======================>');
});

#### featureAbility.hasWindowFocus7+

hasWindowFocus(callback: AsyncCallback<boolean>): void

Checks whether the main window of this ability has the focus. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | 
Callback used to return the result.

If the main window has the focus, **true** is returned. Otherwise, **false** is returned.

 |

**Example**

import { featureAbility } from '@kit.AbilityKit';

featureAbility.hasWindowFocus((error, data) => {
  if (error && error.code !== 0) {
    console.error(\`hasWindowFocus fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`hasWindowFocus success, data: ${JSON.stringify(data)}\`);
  }
});

#### featureAbility.hasWindowFocus7+

hasWindowFocus(): Promise<boolean>

Checks whether the main window of this ability has the focus. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. If the main window has the focus, **true** is returned. Otherwise, **false** is returned. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

featureAbility.hasWindowFocus().then((data) => {
  console.info(\`hasWindowFocus data: ${JSON.stringify(data)}\`);
});

#### featureAbility.getWant

getWant(callback: AsyncCallback<Want>): void

Obtains the Want corresponding to the ability to start. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Want](../../apis-no-longer-maintained/ohos-application-want-want/document.md)\> | Yes | Callback used to return the Want. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

featureAbility.getWant((error, data) => {
  if (error && error.code !== 0) {
    console.error(\`getWant fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`getWant success, data: ${JSON.stringify(data)}\`);
  }
});

#### featureAbility.getWant

getWant(): Promise<Want>

Obtains the Want corresponding to the ability to start. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Want](../../apis-no-longer-maintained/ohos-application-want-want/document.md)\> | Promise used to return the Want. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

featureAbility.getWant().then((data) => {
  console.info(\`getWant data: ${JSON.stringify(data)}\`);
});

#### featureAbility.getContext

getContext(): Context

Obtains the application context.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Return value**

| Type | Description |
| :-- | :-- |
| Context | Application context. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

let context = featureAbility.getContext();
context.getBundleName((error, data) => {
  if (error && error.code !== 0) {
    console.error(\`getBundleName fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`getBundleName success, data: ${JSON.stringify(data)}\`);
  }
});

#### featureAbility.terminateSelf7+

terminateSelf(callback: AsyncCallback<void>): void

Terminates this ability. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

featureAbility.terminateSelf(
  (error) => {
    console.error(\`error: ${JSON.stringify(error)}\`);
  }
)

#### featureAbility.terminateSelf7+

terminateSelf(): Promise<void>

Terminates this ability. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

featureAbility.terminateSelf().then(() => {
  console.info('==========================>terminateSelf=======================>');
}).catch((error: BusinessError) => {
  console.error(\`terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}\`);
});

#### featureAbility.connectAbility7+

connectAbility(request: Want, options:ConnectOptions): number

Connects this ability to a ServiceAbility.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/nbmacmfPTZ-T2iM-6z_VbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BF330CEC4B5FDB63293C3B3E7D1D4D882C46AA490A0CD6681808C5CB82557E0)

For details about the startup rules for the components in the FA model, see [Component Startup Rules (FA Model)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/component-startup-rules-fa).

To connect to a ServiceAbility of another application, the target application must be configured with associated startup (**AssociateWakeUp** set to **true**).

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [Want](../../apis-no-longer-maintained/ohos-application-want-want/document.md) | Yes | ServiceAbility to connect. |
| options | [ConnectOptions](../../dependent-elements-and-definitions/ability/connectoptions/document.md) | Yes | Connection options. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | ID of the connected ServiceAbility. The ID starts from 0 and is incremented by 1 each time a connection is set up. |

**Example**

import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectId = featureAbility.connectAbility(
  {
    deviceId: '',
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(\`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}\`);
    },
    onDisconnect: (element) => {
      console.info(\`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}\`);
    },
    onFailed: (code) => {
      console.error(\`featureAbilityTest ConnectAbility onFailed errCode : ${code}\`);
    },
  },
);

#### featureAbility.disconnectAbility7+

disconnectAbility(connection: number, callback:AsyncCallback<void>): void

Disconnects this ability from a specific ServiceAbility. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | ID of the ServiceAbility to disconnect. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the disconnection is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectId = featureAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(\`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}\`);
    },
    onDisconnect: (element) => {
      console.info(\`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}\`);
    },
    onFailed: (code) => {
      console.error(\`featureAbilityTest ConnectAbility onFailed errCode : ${code}\`);
    },
  },
);

featureAbility.disconnectAbility(connectId, (error) => {
  if (error && error.code !== 0) {
    console.error(\`disconnectAbility fail, connectId: ${connectId}, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`disconnectAbility success, connectId: ${connectId}\`);
  }
});

#### featureAbility.disconnectAbility7+

disconnectAbility(connection: number): Promise<void>

Disconnects this ability from a specific ServiceAbility. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| connection | number | Yes | ID of the ServiceAbility to disconnect. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connectId = featureAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(\`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}\`);
    },
    onDisconnect: (element) => {
      console.info(\`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}\`);
    },
    onFailed: (code) => {
      console.error(\`featureAbilityTest ConnectAbility onFailed errCode : ${code}\`);
    },
  },
);

featureAbility.disconnectAbility(connectId).then(() => {
  console.info('disconnectAbility success');
}).catch((error: BusinessError)=>{
  console.error(\`featureAbilityTest result errCode : ${error.code}\`);
});

#### featureAbility.getWindow7+

getWindow(callback: AsyncCallback<window.Window>): void

Obtains the window corresponding to this ability. This API uses an asynchronous callback to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[window.Window](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md)\> | Yes | Callback used to return the window. |

**Example**

import { featureAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

featureAbility.getWindow((error: BusinessError, data: window.Window) => {
  if (error && error.code !== 0) {
    console.error(\`getWindow fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`getWindow success, data: ${typeof(data)}\`);
  }
});

#### featureAbility.getWindow7+

getWindow(): Promise<window.Window>

Obtains the window corresponding to this ability. This API uses a promise to return the result.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[window.Window](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md)\> | Promise used to return the window. |

**Example**

import { featureAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

featureAbility.getWindow().then((data: window.Window) => {
  console.info(\`getWindow success, data: ${typeof(data)}\`);
}).catch((error: BusinessError)=>{
  console.error(\`getWindow fail, error: ${JSON.stringify(error)}\`);
});

#### AbilityWindowConfiguration7+

Defines the window configuration corresponding to this ability. The configuration is obtained through **featureAbility.AbilityWindowConfiguration**.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW\_MODE\_UNDEFINED | 0 | The PageAbility is in an undefined window display mode. |
| WINDOW\_MODE\_FULLSCREEN | 1 | The PageAbility is in full screen mode. |
| WINDOW\_MODE\_SPLIT\_PRIMARY | 100 | The left screen in horizontal direction or the upper screen in vertical direction is the primary window. |
| WINDOW\_MODE\_SPLIT\_SECONDARY | 101 | The right screen in horizontal direction or the lower screen in vertical direction is the secondary window. |
| WINDOW\_MODE\_FLOATING | 102 | The PageAbility is displayed in floating window mode. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

featureAbility.AbilityWindowConfiguration.WINDOW\_MODE\_UNDEFINED

#### AbilityStartSetting7+

Defines the window property corresponding to this ability. The **abilityStartSetting** property is an object defined in the format of \[**key: string\]: any**, where **key** is an enumerated value of **AbilityStartSetting** and **value** is an enumerated value of **AbilityWindowConfiguration**.

The value is obtained through **featureAbility.AbilityStartSetting**.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Value | Description |
| :-- | :-- | :-- |
| BOUNDS\_KEY | 'abilityBounds' | Ability window size. |
| WINDOW\_MODE\_KEY | 'windowMode' | Ability window display mode. |
| DISPLAY\_ID\_KEY | 'displayId' | Display device ID. |

**Example**

import { featureAbility } from '@kit.AbilityKit';

featureAbility.AbilityStartSetting.BOUNDS\_KEY

#### ErrorCode7+

Enumerates the error codes that may be returned when an ability is started.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_ERROR | 0 | No error. |
| INVALID\_PARAMETER | \-1 | Invalid parameter. |
| ABILITY\_NOT\_FOUND | \-2 | The ability is not found. |
| PERMISSION\_DENY | \-3 | Permission denied. |

#### DataAbilityOperationType7+

Enumerates the operation types of a DataAbility. The DataAbility can use an enumerated value to specify the operation type when operating data in batches.

**Model restriction**: This API can be used only in the FA model.

**System capability**: SystemCapability.Ability.AbilityRuntime.FAModel

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_INSERT | 1 | Insert operation. |
| TYPE\_UPDATE | 2 | Update operation. |
| TYPE\_DELETE | 3 | Deletion operation. |
| TYPE\_ASSERT | 4 | Assert operation. |

#### Context9+

type Context = \_Context

Defines the Context module.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_Context](../app/context-context-base-class-of-the-fa-model/document.md) | Context module. |

#### AppVersionInfo9+

type AppVersionInfo = \_AppVersionInfo

Defines an AppVersionInfo object.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_AppVersionInfo](../app/appversioninfo/document.md) | AppVersionInfo object. |

#### ProcessInfo9+

type ProcessInfo = \_ProcessInfo

Defines a ProcessInfo object.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Model restriction**: This API can be used only in the FA model.

| Type | Description |
| :-- | :-- |
| [\_ProcessInfo](../app/processinfo/document.md) | ProcessInfo object. |
