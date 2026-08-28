# AbilityDelegator

The **AbilityDelegator** module can listen for and manage the lifecycle changes of [UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) through [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instances. For example, you can obtain the current state of a UIAbility (for example, whether the UIAbility has been created or is in the foreground), obtain the UIAbility that currently has the focus, wait for the UIAbility to enter a lifecycle node (for example, the **onForeground** state), start a specified UIAbility, and set the timeout mechanism.

You can obtain **AbilityDelegator** by calling [getAbilityDelegator](../../ohos-app-ability-abilitydelegatorregistry-abilitydelegatorregistry/document.md#abilitydelegatorregistrygetabilitydelegator).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/FmFGfrsoQLeUob9DgI3NjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2488C4F0C5CBF3C1D9FD00153CD0062E986CBB16ED41061B081A5C7B88C07C9)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in [unittest](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/unittest-guidelines).

#### Modules to Import

import { abilityDelegatorRegistry } from '@kit.TestKit';

#### AbilityDelegator

#### \[h2\]addAbilityMonitor9+

addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void

Adds an **AbilityMonitor** instance. This API uses an asynchronous callback to return the result. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the **AbilityMonitor** instance is added, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(\`onAbilityCreateCallback, data: ${JSON.stringify(data)}\`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
  console.error(\`addAbilityMonitor fail, error: ${JSON.stringify(error)}\`);
});

#### \[h2\]addAbilityMonitor9+

addAbilityMonitor(monitor: AbilityMonitor): Promise<void>

Adds an **AbilityMonitor** instance. This API uses a promise to return the result. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};
let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

abilityDelegator.addAbilityMonitor(monitor).then(() => {
  console.info('addAbilityMonitor promise');
});

#### \[h2\]addAbilityMonitorSync10+

addAbilityMonitorSync(monitor: AbilityMonitor): void

Adds an **AbilityMonitor** instance. This API returns the result synchronously. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityMonitorSync failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitorSync(monitor);

#### \[h2\]removeAbilityMonitor9+

removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void

Removes an **AbilityMonitor** instance. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the **AbilityMonitor** instance is removed, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

function onAbilityCreateCallback(data: UIAbility) {
    console.info('onAbilityCreateCallback');
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
    abilityName: 'abilityName',
    onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor, (error: BusinessError) => {
    console.error(\`removeAbilityMonitor fail, error: ${JSON.stringify(error)}\`);
});

#### \[h2\]removeAbilityMonitor9+

removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>

Removes an **AbilityMonitor** instance. This API uses a promise to return the result. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityMonitor failed. |

-   Example

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor).then(() => {
  console.info('removeAbilityMonitor promise');
});

#### \[h2\]removeAbilityMonitorSync10+

removeAbilityMonitorSync(monitor: AbilityMonitor): void

Removes an **AbilityMonitor** instance. This API returns the result synchronously. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityMonitorSync failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitorSync(monitor);

#### \[h2\]waitAbilityMonitor9+

waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void

Waits for the **Ability** instance that matches the **AbilityMonitor** instance to reach the **onCreate** lifecycle state and returns the **Ability** instance. This API uses an asynchronous callback to return the result. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |
| callback | AsyncCallback<[UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the **Ability** instance obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(\`onAbilityCreateCallback, data: ${JSON.stringify(data)}\`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor, (error: BusinessError, data: UIAbility) => {
  if (error) {
    console.error(\`waitAbilityMonitor fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`waitAbilityMonitor success, data: ${JSON.stringify(data)}\`);
  }
});

#### \[h2\]waitAbilityMonitor9+

waitAbilityMonitor(monitor: AbilityMonitor, timeout: number, callback: AsyncCallback<UIAbility>): void

Waits a period of time for the **Ability** instance that matches the **AbilityMonitor** instance to reach the **onCreate** lifecycle state and returns the **Ability** instance. This API uses an asynchronous callback to return the result. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |
| timeout | number | Yes | Maximum waiting time, in milliseconds. The default value is 5000 ms. |
| callback | AsyncCallback<[UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let timeout = 100;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(\`onAbilityCreateCallback, data: ${JSON.stringify(data)}.\`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor, timeout, (error: BusinessError, data: UIAbility) => {
  if (error && error.code !== 0) {
    console.error(\`waitAbilityMonitor fail, error: ${JSON.stringify(error)}\`);
  } else {
    console.info(\`waitAbilityMonitor success, data: ${JSON.stringify(data)}\`);
  }
});

#### \[h2\]waitAbilityMonitor9+

waitAbilityMonitor(monitor: AbilityMonitor, timeout?: number): Promise<UIAbility>

Waits a period of time for the **Ability** instance that matches the **AbilityMonitor** instance to reach the **onCreate** lifecycle state and returns the **Ability** instance. This API uses a promise to return the result. Multi-thread concurrent calls are not supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) | Yes | [AbilityMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitymonitor/document.md) instance. |
| timeout | number | No | Maximum waiting time, in milliseconds. The default value is 5000 ms. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)\> | Promise used to return the **Ability** instance obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor).then((data: UIAbility) => {
  console.info('waitAbilityMonitor promise');
});

#### \[h2\]getAppContext9+

getAppContext(): Context

Obtains the application context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | [Context](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

let context = abilityDelegator.getAppContext();

#### \[h2\]getAbilityState9+

getAbilityState(ability: UIAbility): number

Obtains the lifecycle state of an ability.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ability | [UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) | Yes | Target ability. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Lifecycle state of the ability, For details about the state values, see [AbilityLifecycleState](../../ohos-app-ability-abilitydelegatorregistry-abilitydelegatorregistry/document.md#abilitylifecyclestate). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  let state = abilityDelegator.getAbilityState(ability);
  console.info(\`getAbilityState ${state}\`);
});

#### \[h2\]getCurrentTopAbility9+

getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void

Obtains the top ability of this application. This API uses an asynchronous callback to return the result. It cannot be called in the worker thread.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)\> | Yes | Callback used to return the result. If the top ability is obtained, **err** is **undefined** and **data** is the **Ability** instance obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling GetCurrentTopAbility failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
});

#### \[h2\]getCurrentTopAbility9+

getCurrentTopAbility(): Promise<UIAbility>

Obtains the top ability of this application. This API uses a promise to return the result. It cannot be called in the worker thread.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md)\> | Promise used to return the top ability. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 16000100 | Calling GetCurrentTopAbility failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility().then((data: UIAbility) => {
  console.info('getCurrentTopAbility promise');
  ability = data;
});

#### \[h2\]startAbility9+

startAbility(want: Want, callback: AsyncCallback<void>): void

Starts an ability. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | **Want** parameter for starting the ability. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the ability is started, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
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

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let want: Want = {
  bundleName: 'bundleName',
  abilityName: 'abilityName'
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.startAbility(want, (err: BusinessError, data: void) => {
  console.info('startAbility callback');
});

#### \[h2\]startAbility9+

startAbility(want: Want): Promise<void>

Starts an ability. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | **Want** parameter for starting the ability. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
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

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let want: Want = {
  bundleName: 'bundleName',
  abilityName: 'abilityName'
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.startAbility(want).then((data: void) => {
  console.info('startAbility promise');
});

#### \[h2\]doAbilityForeground9+

doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void

Schedules the lifecycle state of an ability to **Foreground**. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ability | [UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) | Yes | Target ability. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the ability lifecycle state is changed to **Foreground**, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityForeground failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityForeground(ability, (err: BusinessError) => {
    console.info("doAbilityForeground callback");
  });
});

#### \[h2\]doAbilityForeground9+

doAbilityForeground(ability: UIAbility): Promise<void>

Schedules the lifecycle state of an ability to **Foreground**. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ability | [UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) | Yes | Target ability. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityForeground failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityForeground(ability).then(() => {
    console.info("doAbilityForeground promise");
  });
});

#### \[h2\]doAbilityBackground9+

doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void

Schedules the lifecycle state of an ability to **Background**. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ability | [UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) | Yes | Target ability. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the ability lifecycle state is changed to **Background**, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityBackground failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityBackground(ability, (err: BusinessError) => {
    console.info("doAbilityBackground callback");
  });
});

#### \[h2\]doAbilityBackground9+

doAbilityBackground(ability: UIAbility): Promise<void>

Schedules the lifecycle state of an ability to **Background**. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ability | [UIAbility](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) | Yes | Target ability. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling DoAbilityBackground failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityBackground(ability).then(() => {
    console.info("doAbilityBackground promise");
  });
});

#### \[h2\]printSync9+

printSync(msg: string): void

Prints log information to the unit test console.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msg | string | Yes | Log string. The value contains a maximum of 10,000 characters. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.printSync(msg);

#### \[h2\]print

print(msg: string, callback: AsyncCallback<void>): void

Prints log information to the unit test console. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msg | string | Yes | Log string. The value contains a maximum of 10,000 characters. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the log information is printed to the unit test console, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.print(msg, (err: BusinessError) => {
  console.info('print callback');
});

#### \[h2\]print

print(msg: string): Promise<void>

Prints log information to the unit test console. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msg | string | Yes | Log string. The value contains a maximum of 10,000 characters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.print(msg).then(() => {
  console.info('print promise');
});

#### \[h2\]executeShellCommand

executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void

Executes a shell command. This API uses an asynchronous callback to return the result.

Only the following shell commands are supported: aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, and pidof.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cmd | string | Yes | Shell command string. |
| callback | AsyncCallback<[ShellCmdResult](../shellcmdresult/document.md#shellcmdresult-1)\> | Yes | Callback used to return the result. If the shell command is executed, **err** is **undefined** and **data** is the execution result obtained. Otherwise, **err** is an error object. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  console.info('executeShellCommand callback');
});

#### \[h2\]executeShellCommand

executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void

Executes a shell command with the timeout period specified. This API uses an asynchronous callback to return the result.

Only the following shell commands are supported: aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, and pidof.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cmd | string | Yes | Shell command string. |
| timeoutSecs | number | Yes | Command timeout period, in seconds. |
| callback | AsyncCallback<[ShellCmdResult](../shellcmdresult/document.md#shellcmdresult-1)\> | Yes | Callback used to return the result. If the shell command is executed, **err** is **undefined** and **data** is the execution result obtained. Otherwise, **err** is an error object. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, timeout, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  console.info('executeShellCommand callback');
});

#### \[h2\]executeShellCommand

executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>

Executes a shell command with the timeout period specified. This API uses a promise to return the result.

Only the following shell commands are supported: aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, and pidof.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cmd | string | Yes | Shell command string. |
| timeoutSecs | number | No | Command timeout period, in seconds. The default value is **0**, indicating that the timeout period is not set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ShellCmdResult](../shellcmdresult/document.md#shellcmdresult-1)\> | Promise used to return a [ShellCmdResult](../shellcmdresult/document.md#shellcmdresult-1) object. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, timeout).then((data) => {
  console.info('executeShellCommand promise');
});

#### \[h2\]finishTest9+

finishTest(msg: string, code: number, callback: AsyncCallback<void>): void

Finishes the test and prints log information to the unit test console. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msg | string | Yes | Log string. |
| code | number | Yes | Log code. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the test finishes and the log information is printed to the unit test console, **err** is undefined. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling FinishTest failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.finishTest(msg, 0, (err: BusinessError) => {
  console.info('finishTest callback');
});

#### \[h2\]finishTest9+

finishTest(msg: string, code: number): Promise<void>

Finishes the test and prints log information to the unit test console. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msg | string | Yes | Log string. |
| code | number | Yes | Log code. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling FinishTest failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.finishTest(msg, 0).then(() => {
  console.info('finishTest promise');
});

#### \[h2\]addAbilityStageMonitor9+

addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void

Adds an **AbilityStageMonitor** instance to monitor the lifecycle state changes of an ability stage. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the **AbilityStageMonitor** instance is added, **err** is undefined. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityStageMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  console.info('addAbilityStageMonitor callback');
});

#### \[h2\]addAbilityStageMonitor9+

addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>

Adds an **AbilityStageMonitor** instance to monitor the lifecycle state changes of an ability stage. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityStageMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then(() => {
  console.info('addAbilityStageMonitor promise');
});

#### \[h2\]addAbilityStageMonitorSync10+

addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void

Adds an **AbilityStageMonitor** instance to monitor the lifecycle state changes of an ability stage. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling AddAbilityStageMonitorSync failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitorSync({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
});

#### \[h2\]removeAbilityStageMonitor9+

removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void

Removes an **AbilityStageMonitor** instance from the application memory. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the **AbilityStageMonitor** instance is removed, **err** is undefined. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityStageMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  console.info('removeAbilityStageMonitor callback');
});

#### \[h2\]removeAbilityStageMonitor9+

removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>

Removes an **AbilityStageMonitor** instance from the application memory. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityStageMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then(() => {
  console.info('removeAbilityStageMonitor promise');
});

#### \[h2\]removeAbilityStageMonitorSync10+

removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void

Removes an **AbilityStageMonitor** instance from the application memory. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling RemoveAbilityStageMonitorSync failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitorSync({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
});

#### \[h2\]waitAbilityStageMonitor9+

waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void

Returns an **AbilityStage** instance that matches the conditions set in an **AbilityStageMonitor** instance. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |
| callback | AsyncCallback<AbilityStage> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and data is the [AbilityStage](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md) instance obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityStageMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError, data: AbilityStage) => {
  console.info('waitAbilityStageMonitor callback');
});

#### \[h2\]waitAbilityStageMonitor9+

waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: number): Promise<AbilityStage>

Returns an **AbilityStage** instance that matches the conditions set in an **AbilityStageMonitor** instance. You can specify the timeout period. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |
| timeout | number | No | Maximum waiting time, in milliseconds. The default value is 5000 ms. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<AbilityStage> | Promise used to return the [AbilityStage](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md) instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityStageMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then((data: AbilityStage) => {
  console.info('waitAbilityStageMonitor promise');
});

#### \[h2\]waitAbilityStageMonitor9+

waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: number, callback: AsyncCallback<AbilityStage>): void

Returns an **AbilityStage** instance that matches the conditions set in an **AbilityStageMonitor** instance within the specified timeout period. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitor | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) | Yes | [AbilityStageMonitor](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/abilitystagemonitor/document.md) instance. |
| timeout | number | Yes | Maximum waiting time, in milliseconds. The default value is 5000 ms. |
| callback | AsyncCallback<AbilityStage> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and data is the [AbilityStage](../../../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md) instance obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000100 | Calling WaitAbilityStageMonitor failed. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, timeout, (err: BusinessError, data: AbilityStage) => {
  console.info('waitAbilityStageMonitor callback');
});

#### \[h2\]setMockList11+

setMockList(mockList: Record<string, string>): void

Sets a list of mock data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mockList | Record<string, string> | Yes | Key-value object of the mock, where **key** is the target path to be replaced and **value** is the path of the mock implementation to be used for the replacement. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Ability Error Codes](../../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

**Example**

import { abilityDelegatorRegistry } from '@kit.TestKit';

let mockList: Record<string, string> = {
  '@ohos.router': 'src/main/mock/ohos/router.mock',
  'common.time': 'src/main/mock/common/time.mock',
};
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.setMockList(mockList);
