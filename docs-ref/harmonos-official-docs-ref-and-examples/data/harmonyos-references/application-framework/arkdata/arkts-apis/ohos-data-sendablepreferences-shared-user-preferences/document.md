# @ohos.data.sendablePreferences (Shared User Preferences)

The **sendablePreferences** module provides APIs for processing data in the form of key-value (KV) pairs, including querying, modifying, and persisting KV pairs.

In the KV pairs, the key must be a string, and the value can be a number, a string, a Boolean value, a bigint, or a serializable object.

The persistent files of the shared user preferences are stored in the [preferencesDir](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#obtaining-application-file-paths) directory. Before creating a preferences object, ensure that the **preferencesDir** path can be read and written. The [encryption level](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-contextconstant-context-related-constants/document.md#areamode) of the persistent file directory determines the access to the files. For details, see [Application File Directory and Application File Path](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory#application-file-directory-and-application-file-path).

Sendable preferences can be passed between concurrent ArkTS instances (including the main thread and TaskPool or Worker threads) by reference. It allows for higher performance than [user preferences](../ohos-data-preferences-user-preferences/document.md). For more information, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/3l7xF28nRRe1FyW7DwC0yA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE8DF4741D3829CE4AF6A86811E8C9F158A433E57AA2AF71C12D66481BDF7A41)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The shared user preferences are not thread-safe and may cause file damage and data loss when used in multi-process scenarios. Do not use it in multi-process scenarios.

#### Modules to Import

import { sendablePreferences } from '@kit.ArkData';

#### Constants

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| MAX\_KEY\_LENGTH | number | Yes | Maximum length of a key, which is 1024 bytes. |
| MAX\_VALUE\_LENGTH | number | Yes | Maximum length of a value, which is 16 MB. |

#### sendablePreferences.getPreferences

getPreferences(context: Context, options: Options): Promise<Preferences>

Obtains a **Preferences** instance. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| options | [Options](#options) | Yes | Configuration options of the **Preferences** instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Preferences](#preferences)\> | 
Promise used to return the **Preferences** instance obtained.

This instance inherits from [ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) and can be passed between concurrent ArkTS instances (including the main thread and the TaskPool or Worker threads) by reference. For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let preferences: sendablePreferences.Preferences;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.getPreferences(this.context, options);
    promise.then((object: sendablePreferences.Preferences) => {
      preferences = object;
      console.info("Succeeded in getting preferences.");
    }).catch((err: BusinessError) => {
      console.error(\`Failed to get preferences. code: ${err.code}, message: ${err.message}\`);
    });
  }
}

#### sendablePreferences.getPreferencesSync

getPreferencesSync(context: Context, options: Options): Preferences

Obtains a **Preferences** instance. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| options | [Options](#options) | Yes | Configuration options of the **Preferences** instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Preferences](#preferences) | 
**Preferences** instance obtained.

This instance inherits from [ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) and can be passed between concurrent ArkTS instances (including the main thread and the TaskPool or Worker threads) by reference. For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

let preferences: sendablePreferences.Preferences;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    preferences = sendablePreferences.getPreferencesSync(this.context, options);
  }
}

#### sendablePreferences.deletePreferences

deletePreferences(context: Context, options: Options): Promise<void>

Deletes a specified **Preferences** instance from the cache. If the **Preferences** instance has a corresponding persistent file, the persistent file is also deleted. This API uses a promise to return the result.

Avoid using a deleted **Preferences** instance to perform data operations, which may cause data inconsistency.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| options | [Options](#options) | Yes | Configuration options of the **Preferences** instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.deletePreferences(this.context, options);
    promise.then(() => {
      console.info("Succeeded in deleting preferences.");
    }).catch((err: BusinessError) => {
      console.error(\`Failed to delete preferences. code: ${err.code}, message: ${err.message}\`);
    });
  }
}

#### sendablePreferences.removePreferencesFromCache

removePreferencesFromCache(context: Context, options: Options): Promise<void>

Removes a **Preferences** instance from the cache. This API uses a promise to return the result.

After an application calls [getPreferences](#sendablepreferencesgetpreferences) for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the application calls [getPreferences](#sendablepreferencesgetpreferences) again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API is called to remove the instance from the cache, calling **getPreferences** again will read data from the persistent file and create a **Preferences** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| options | [Options](#options) | Yes | Configuration options of the **Preferences** instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    let promise = sendablePreferences.removePreferencesFromCache(this.context, options);
    promise.then(() => {
      console.info("Succeeded in removing preferences.");
    }).catch((err: BusinessError) => {
      console.error(\`Failed to remove preferences. code: ${err.code}, message: ${err.message}\`);
    });
  }
}

#### sendablePreferences.removePreferencesFromCacheSync

removePreferencesFromCacheSync(context: Context, options: Options):void

Removes a **Preferences** instance from the cache. This API returns the result synchronously.

After an application calls [getPreferences](#sendablepreferencesgetpreferences) for the first time to obtain a **Preferences** instance, the obtained **Preferences** instance is cached. When the application calls [getPreferences](#sendablepreferencesgetpreferences) again, the **Preferences** instance will be read from the cache instead of from the persistent file. After this API is called to remove the instance from the cache, calling **getPreferences** again will read data from the persistent file and create a **Preferences** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md) | Yes | Application context. |
| options | [Options](#options) | Yes | Configuration options of the **Preferences** instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: sendablePreferences.Options = { name: 'myStore' };
    sendablePreferences.removePreferencesFromCacheSync(this.context, options);
  }
}

#### Options

Represents the configuration options of a **Preferences** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the **Preferences** instance. |
| dataGroupId | string|null | No | Yes | 
Application group ID. Currently, this parameter is not supported.

This parameter is optional. A **Preferences** instance will be created in the sandbox path corresponding to the specified **dataGroupId**. If this parameter is not specified, the **Preferences** instance is created in the sandbox directory of the application.

**Model restriction**: This attribute can be used only in the stage model.

 |

#### Preferences

Provides APIs for obtaining and modifying **Preferences** instances. **Preferences** inherits from [ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) and can be passed between concurrent ArkTS instances (including the main thread and the TaskPool or Worker threads) by reference.

Before calling any API of **Preferences**, obtain a **Preferences** instance by using [sendablePreferences.getPreferences](#sendablepreferencesgetpreferences).

#### \[h2\]get

get(key: string, defValue: lang.ISendable): Promise<lang.ISendable>

Obtains the value of a key from this **Preferences** instance. This API uses a promise to return the result. If the value is null or is not of the default value type, **defValue** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be obtained. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |
| defValue | [lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) | Yes | Default value to be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable)\> | 
Promise used to return the value obtained.

This instance inherits from [ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) and can be passed between concurrent ArkTS instances (including the main thread and the TaskPool or Worker threads) by reference. For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let promise = preferences.get('startup', 'default');
promise.then((data: lang.ISendable) => {
  let dataStr = data as string;
  console.info(\`Succeeded in getting value of 'startup'. Data: ${dataStr}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get value of 'startup'. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]getSync

getSync(key: string, defValue: lang.ISendable): lang.ISendable

Obtains the value of a key from this **Preferences** instance. This API returns the result synchronously. If the value is null or is not of the default value type, **defValue** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be obtained. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |
| defValue | [lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) | Yes | Default value to be returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) | 
Value obtained.

This instance inherits from [ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) and can be passed between concurrent ArkTS instances (including the main thread and the TaskPool or Worker threads) by reference. For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { lang } from '@kit.ArkTS';
let value: lang.ISendable = preferences.getSync('startup', 'default');

#### \[h2\]getAll

getAll(): Promise<lang.ISendable>

Obtains all KV pairs from this **Preferences** instance. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable)\> | 
Promise used to return the KV pairs obtained.

This object inherits from [ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) and can be passed between concurrent ArkTS instances (including the main thread and the TaskPool or Worker threads) by reference. For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let promise = preferences.getAll();
promise.then((keyValues: lang.ISendable) => {
  for (let value of Object.keys(keyValues)) {
    console.info("getAll " + JSON.stringify(value));
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to get all key-values. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]getAllSync

getAllSync(): lang.ISendable

Obtains all KV pairs from this **Preferences** instance. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) | 
All KV pairs obtained.

This object inherits from [ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) and can be passed between concurrent ArkTS instances (including the main thread and the TaskPool or Worker threads) by reference. For details, see [Using Sendable Objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sendable-guide).

 |

**Error codes**

For details about the error codes, see [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15500000 | Inner error. |

**Example**

import { lang } from '@kit.ArkTS';

let keyValues: lang.ISendable = preferences.getAllSync();
for (let value of Object.keys(keyValues)) {
  console.info("getAll " + JSON.stringify(value));
}

#### \[h2\]put

put(key: string, value: lang.ISendable): Promise<void>

Writes data to this **Preferences** instance. This API uses a promise to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/XtDWkUNJQCCg0m3pJqs9LQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D20630A29B07D1E108128F206FBC4170EDBAFD8554968AA04F9BFD9469711506)

If the value contains a string that is not in UTF-8 format, store it in a Uint8Array. Otherwise, the persistent file may be damaged due to format errors.

If the key already exists, **put()** overwrites the value. You can use **hasSync()** to check whether the KV pair exists.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be modified. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |
| value | [lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) | Yes | Value to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.put('startup', 'auto');
promise.then(() => {
  console.info("Succeeded in putting value of 'startup'.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to put value of 'startup'. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]putSync

putSync(key: string, value: lang.ISendable): void

Writes data to this **Preferences** instance. This API returns the result synchronously. You can use [flush](#flush) to persist the **Preferences** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sRi5AL20SrG8M2EGsN717w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96FE652FEF5672270A6A7E568EFBDDDC7C5FD651CE980328EA5A910D7046FA56)

If the value contains a string that is not in UTF-8 format, store it in a Uint8Array. Otherwise, the persistent file may be damaged due to format errors.

If the key already exists, **putSync()** overwrites the value. You can use **hasSync()** to check whether the KV pair exists.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be modified. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |
| value | [lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable) | Yes | Value to write. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

preferences.putSync('startup', 'auto');

#### \[h2\]has

has(key: string): Promise<boolean>

Checks whether this **Preferences** instance contains the KV pair of the given key. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be checked. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the **Preferences** instance contains the KV pair; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.has('startup');
promise.then((val: boolean) => {
  if (val) {
    console.info("The key 'startup' is contained.");
  } else {
    console.error("The key 'startup' does not contain.");
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to check the key 'startup'. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]hasSync

hasSync(key: string): boolean

Checks whether this **Preferences** instance contains the KV pair of the given key. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be checked. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means the **Preferences** instance contains the KV pair; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

let isExist: boolean = preferences.hasSync('startup');
if (isExist) {
  console.info("The key 'startup' is contained.");
} else {
  console.error("The key 'startup' does not contain.");
}

#### \[h2\]delete

delete(key: string): Promise<void>

Deletes a KV pair from this **Preferences** instance. This API uses a promise to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be deleted. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.delete('startup');
promise.then(() => {
  console.info("Succeeded in deleting the key 'startup'.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to delete the key 'startup'. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]deleteSync

deleteSync(key: string): void

Deletes a KV pair from this **Preferences** instance. This API returns the result synchronously. You can use [flush](#flush) to persist the **Preferences** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Key to be deleted. The value cannot be empty, and the maximum length is 1024 bytes. For details, see [MAX\_KEY\_LENGTH](#constants). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

preferences.deleteSync('startup');

#### \[h2\]flush

flush(): Promise<void>

Flushes the data in this **Preferences** instance to the persistent file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/s3SQpWm_SeqKptlPbPumjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=103D0D244E6EFE3387C7EA51B6F89752B436421ED1EA9EE6E277A7129F549BE6)

If no data is modified or the modified data is the same as the cached data, the persistence file will not be updated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.flush();
promise.then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to flush. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]flushSync14+

flushSync(): void

Flushes the data in the cached **Preferences** instance to the persistent file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/6ksKZWXKRA6M2a_rOhkFXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC8F321BF1CB01F4EB4EBD3B9DAEC1F99E201703C202E107647F96DE9A7E805E)

If no data is modified or the modified data is the same as the cached data, the persistence file will not be updated.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Error codes**

For details about the error codes, see [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15500000 | Inner error. |

**Example**

preferences.flushSync();

#### \[h2\]clear

clear(): Promise<void>

Clears this **Preferences** instance. This API uses a promise to return the result. You can use [flush](#flush) to persist the **Preferences** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let promise = preferences.clear();
promise.then(() => {
  console.info("Succeeded in clearing.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to clear. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]clearSync

clearSync(): void

Clears this **Preferences** instance. This API returns the result synchronously. You can use [flush](#flush) to persist the **Preferences** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Error codes**

For details about the error codes, see [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15500000 | Inner error. |

**Example**

preferences.clearSync();

#### \[h2\]on('change')

on(type: 'change', callback: Callback<string>): void

Subscribes to data changes. The registered callback will be invoked to return the new value if the data change is [flushed](#flush).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Rqg1ZJFwQLiJniAWttOOpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D645B812AEB54A1740D1FD5969E61F278979F97CF3D1D5DE4B2AC3A4D8C592B5)

After [removePreferencesFromCache](#sendablepreferencesremovepreferencesfromcache) or [deletePreferences](#sendablepreferencesdeletepreferences) is called, the data change subscription will be automatically canceled. After [getPreferences](#sendablepreferencesgetpreferences) is called again, you need to subscribe to data changes again.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | Callback<string> | Yes | Callback used to return the key whose value is changed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('change', observer);
preferences.putSync('startup', 'manual');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to flush. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('multiProcessChange')

on(type: 'multiProcessChange', callback: Callback<string>): void

Subscribes to data changes between processes. When multiple processes hold the same preference file, calling [flush](#flush) in any process (including the current process) will trigger the callback in this API.

This API is provided for applications that have applied for [dataGroupId](#options). Avoid using this API for the applications that have not applied for **dataGroupId** because calling it in multiple process may damage the persistent files and cause data loss.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/RvOsrDsdTzqnOug4B8Bhjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEB528230B1FAB3D8300FF9CDC2004D3B191CC7D7ECF0EF6D733849E572B40BC)

The maximum number of subscriptions for inter-process data change of the same persistent file for the current process is 50. Once the limit is reached, the subscription will fail. You are advised to cancel the subscription in a timely manner after the callback is triggered.

After [removePreferencesFromCache](#sendablepreferencesremovepreferencesfromcache) or [deletePreferences](#sendablepreferencesdeletepreferences) is called, the data change subscription will be automatically canceled. After [getPreferences](#sendablepreferencesgetpreferences) is called again, you need to subscribe to data changes again.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'multiProcessChange'**, which indicates inter-process data changes. |
| callback | Callback<string> | Yes | Callback used to return the key whose value is changed. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500019 | Failed to obtain the subscription service. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('multiProcessChange', observer);
preferences.putSync('startup', 'manual');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to flush. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]on('dataChange')

on(type: 'dataChange', keys: Array<string>, callback: Callback<lang.ISendable>): void

Subscribes to changes of specific data. The registered callback will be invoked only after the values of the specified keys are changed and [flushed](#flush).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/RLjDMV9BQTKK4w9i61mwTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9348EEAD06529A5E14559CBA1F7BDA6FA0EB26128B0F1A2596B28E6E18064526)

After [removePreferencesFromCache](#sendablepreferencesremovepreferencesfromcache) or [deletePreferences](#sendablepreferencesdeletepreferences) is called, the data change subscription will be automatically canceled. After [getPreferences](#sendablepreferencesgetpreferences) is called again, you need to subscribe to data changes again.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| keys | Array<string> | Yes | Keys to be observed. |
| callback | Callback<[lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable)\> | Yes | Callback used to return the KV pairs changed. The keys are the keys observed, and the values are the new values. The values support the following types: number, string, boolean, bigint, and serializable object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let observer = (data: lang.ISendable) => {
  console.info(\`observer : ${data}\`);
};
let keys = \['name', 'age'\];
preferences.on('dataChange', keys, observer);
preferences.putSync('name', 'xiaohong');
preferences.putSync('weight', 125);
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error(\`Failed to flush. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('change')

off(type: 'change', callback?: Callback<string>): void

Unsubscribes from data changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | Callback<string> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for data changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('change', observer);
preferences.putSync('startup', 'auto');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
  preferences.off('change', observer);
}).catch((err: BusinessError) => {
  console.error(\`Failed to flush. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('multiProcessChange')

off(type: 'multiProcessChange', callback?: Callback<string>): void

Unsubscribes from inter-process data changes.

This API is provided for applications that have applied for [dataGroupId](#options). Avoid using this API for the applications that have not applied for **dataGroupId** because calling it in multiple process may damage the persistent files and cause data loss.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'multiProcessChange'**, which indicates inter-process data changes. |
| callback | Callback<string> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for data changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
};
preferences.on('multiProcessChange', observer);
preferences.putSync('startup', 'auto');
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
  preferences.off('multiProcessChange', observer);
}).catch((err: BusinessError) => {
  console.error(\`Failed to flush. code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]off('dataChange')

off(type: 'dataChange', keys: Array<string>, callback?: Callback<lang.ISendable>): void

Unsubscribes from changes of specific data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'dataChange'**, which indicates data changes. |
| keys | Array<string> | Yes | Keys to be unsubscribed from. If this parameter is not specified, this API unsubscribes from the changes of all keys. |
| callback | Callback<[lang.ISendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#isendable)\> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the changes of the specified data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [User Preference Error Codes](../../error-codes/user-preference-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { lang } from '@kit.ArkTS';

let observer = (data: lang.ISendable) => {
  console.info(\`observer : ${data}\`);
};
let keys = \['name', 'age'\];
preferences.on('dataChange', keys, observer);
preferences.putSync('name', 'xiaohong');
preferences.putSync('weight', 125);
preferences.flush().then(() => {
  console.info("Succeeded in flushing.");
  preferences.off('dataChange', keys, observer);
}).catch((err: BusinessError) => {
  console.error(\`Failed to flush. code: ${err.code}, message: ${err.message}\`);
});
