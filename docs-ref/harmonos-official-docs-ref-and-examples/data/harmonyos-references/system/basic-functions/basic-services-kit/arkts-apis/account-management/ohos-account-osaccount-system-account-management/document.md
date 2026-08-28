# @ohos.account.osAccount (System Account Management)

The **osAccount** module provides basic capabilities for managing system (OS) accounts, including adding, deleting, querying, setting, subscribing to, and enabling a system account.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/fumCWhWLRUujkqJK7oaZwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=069ABECC58E6F1D39C52394DBE3B0826A94C6A256E3E3BB0C34A852556AB2B44)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { osAccount } from '@kit.BasicServicesKit';

#### osAccount.getAccountManager

getAccountManager(): AccountManager

Obtains an **AccountManager** instance.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| [AccountManager](#accountmanager) | **AccountManager** instance obtained. |

**Example**

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();

#### OsAccountType

Enumerates the system account types.

**System capability**: SystemCapability.Account.OsAccount

| Name | Value | Description |
| :-- | :-- | :-- |
| ADMIN | 0 | Administrator account. |
| NORMAL | 1 | Normal account. |
| GUEST | 2 | Guest account. |

#### AccountManager

Provides APIs for managing system accounts.

#### \[h2\]checkMultiOsAccountEnabled9+

checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void

Checks whether multiple system accounts are supported. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means multiple system accounts are supported; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkMultiOsAccountEnabled((err: BusinessError, isEnabled: boolean) => {
    if (err) {
      console.error(\`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkMultiOsAccountEnabled9+

checkMultiOsAccountEnabled(): Promise<boolean>

Checks whether multiple system accounts are supported. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means multiple system accounts are supported; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.checkMultiOsAccountEnabled().then((isEnabled: boolean) => {
    console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(\`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountActivated(deprecated)

checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void

Checks whether a system account is activated. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/e8GbBjxjSqCbSSS8uFSwog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB3B98EC6B6F86B764E5F45664F0056990980D6072941ADEEA4C75EF70B507A9)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**: Check whether system account 100 is activated.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountActivated(localId, (err: BusinessError, isActivated: boolean) => {
    if (err) {
      console.error(\`checkOsAccountActivated failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('checkOsAccountActivated successfully, isActivated:' + isActivated);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountActivated exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountActivated(deprecated)

checkOsAccountActivated(localId: number): Promise<boolean>

Checks whether a system account is activated. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/BL9X65wWSm6WQpOSdof7qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=693B09DB0F492AE4FE6216350D9214A509AAB9F4CC4386E3E38E54A235AA3C20)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**: Check whether system account 100 is activated.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountActivated(localId).then((isActivated: boolean) => {
    console.info('checkOsAccountActivated successfully, isActivated: ' + isActivated);
  }).catch((err: BusinessError) => {
    console.error(\`checkOsAccountActivated failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountActivated exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]isOsAccountConstraintEnabled11+

isOsAccountConstraintEnabled(constraint: string): Promise<boolean>

Checks whether a constraint is enabled for this system account. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| constraint | string | Yes | [Constraint](#constraints) to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**: Check whether system account 100 is forbidden to use Wi-Fi.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let constraint: string = 'constraint.wifi';
try {
  accountManager.isOsAccountConstraintEnabled(constraint).then((isEnabled: boolean) => {
    console.info('isOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(\`isOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`isOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountConstraintEnabled(deprecated)

checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void

Checks whether the specified constraint is enabled for a system account. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/YMBWvFyBQfmOxfC_0PwsyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00260F29BE75084D35D91449E5DE59B7D69059C12A97E970B54A0EE230A6F658)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| constraint | string | Yes | [Constraint](#constraints) to check. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId or constraint. |
| 12300003 | Account not found. |

**Example**: Check whether system account 100 is forbidden to use Wi-Fi.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
try {
  accountManager.checkOsAccountConstraintEnabled(localId, constraint, (err: BusinessError, isEnabled: boolean)=>{
    if (err) {
      console.error(\`checkOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('checkOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountConstraintEnabled(deprecated)

checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>

Checks whether the specified constraint is enabled for a system account. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/p_Srgz60SrqbaM4LqnyBfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26D357605DF9C69556C050D884389ADE7C9C361C2E0BF9A9577962DC54142F4F)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| constraint | string | Yes | [Constraint](#constraints) to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId or constraint. |
| 12300003 | Account not found. |

**Example**: Check whether system account 100 is forbidden to use Wi-Fi.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
try {
  accountManager.checkOsAccountConstraintEnabled(localId, constraint).then((isEnabled: boolean) => {
    console.info('checkOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(\`checkOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountTestable9+

checkOsAccountTestable(callback: AsyncCallback<boolean>): void

Checks whether this system account is a test account. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the account is a test account; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountTestable((err: BusinessError, isTestable: boolean) => {
    if (err) {
      console.error(\`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountTestable code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountTestable9+

checkOsAccountTestable(): Promise<boolean>

Checks whether this system account is a test account. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the account is a test account; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountTestable().then((isTestable: boolean) => {
    console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
  }).catch((err: BusinessError) => {
    console.error(\`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountTestable exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]isOsAccountUnlocked11+

isOsAccountUnlocked(): Promise<boolean>

Checks whether this system account is unlocked. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the system account is unlocked; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.isOsAccountUnlocked().then((isVerified: boolean) => {
    console.info('isOsAccountUnlocked successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(\`isOsAccountUnlocked failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`isOsAccountUnlocked exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountVerified(deprecated)

checkOsAccountVerified(callback: AsyncCallback<boolean>): void

Checks whether a system account has been verified. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/3vRikQHwQJmSHK5SJqq3zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25A52D603D1ED0DA702ADD96DB3B937FE022CD96BEB3743EDE9A500B675355A7)

This API is supported since API version 9 and deprecated since API version 11. Use [isOsAccountUnlocked](#isosaccountunlocked11) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the system account has been verified; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountVerified((err: BusinessError, isVerified: boolean) => {
    if (err) {
      console.error(\`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountVerified(deprecated)

checkOsAccountVerified(): Promise<boolean>

Checks whether this system account has been verified. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/eX_CzG_8SO-MqP4FtVN8ZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85892241D568FBC42713A40ED67D71DDA144E71384FA87B143877470A5631C21)

This API is supported since API version 9 and deprecated since API version 11. Use [isOsAccountUnlocked](#isosaccountunlocked11) instead.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means this system account has been verified; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountVerified().then((isVerified: boolean) => {
    console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(\`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountVerified(deprecated)

checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void

Checks whether a system account has been verified. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/OBz9wq6NQpWMaB4Opo9oSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C25F4F1810266E087938991C0B15A0A967831A795A8BBE1D69D24FD6184E897E)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the system account has been verified; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
    if (err) {
      console.error(\`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]checkOsAccountVerified(deprecated)

checkOsAccountVerified(localId: number): Promise<boolean>

Checks whether a system account has been verified. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Hk3qnOK0RQG_4a_QX8psEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC6B0540A77C1422F23210DEE61DBA2AC189C281F5AD323B4280FD5D01D28B14)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. If this parameter is not specified, this API checks whether the current system account has been verified. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the system account has been verified; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountVerified(localId).then((isVerified: boolean) => {
    console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(\`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountCount9+

getOsAccountCount(callback: AsyncCallback<number>): void

Obtains the number of system accounts created. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the number of created system accounts. If the operation fails, **err** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountCount((err: BusinessError, count: number) => {
    if (err) {
      console.error(\`getOsAccountCount failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('getOsAccountCount successfully, count: ' + count);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountCount exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountCount9+

getOsAccountCount(): Promise<number>

Obtains the number of system accounts created. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of created system accounts. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountCount().then((count: number) => {
    console.info('getOsAccountCount successfully, count: ' + count);
  }).catch((err: BusinessError) => {
    console.error(\`getOsAccountCount failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountCount exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalId9+

getOsAccountLocalId(callback: AsyncCallback<number>): void

Obtains the ID of the system account to which the current process belongs. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account ID obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalId((err: BusinessError, localId: number) => {
    if (err) {
      console.error(\`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('getOsAccountLocalId successfully, localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalId9+

getOsAccountLocalId(): Promise<number>

Obtains the ID of the system account to which the current process belongs. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the system account ID obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalId().then((localId: number) => {
    console.info('getOsAccountLocalId successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(\`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalIdForUid9+

getOsAccountLocalIdForUid(uid: number, callback: AsyncCallback<number>): void

Obtains the system account ID based on the process UID. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | Process UID. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account ID obtained. Otherwise, **data** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid uid. |

**Example**: Obtain the ID of the system account whose process UID is **12345678**.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
try {
  accountManager.getOsAccountLocalIdForUid(uid, (err: BusinessError, localId: number) => {
    if (err) {
      console.error(\`getOsAccountLocalIdForUid failed, code is ${err.code}, message is ${err.message}\`);
    }
    console.info('getOsAccountLocalIdForUid successfully, localId: ' + localId);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalIdForUid exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalIdForUid9+

getOsAccountLocalIdForUid(uid: number): Promise<number>

Obtains the system account ID based on the process UID. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | Process UID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the system account ID obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid uid. |

**Example**: Obtain the ID of the system account whose process UID is **12345678**.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
try {
  accountManager.getOsAccountLocalIdForUid(uid).then((localId: number) => {
    console.info('getOsAccountLocalIdForUid successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(\`getOsAccountLocalIdForUid failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalIdForUid exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalIdForUidSync10+

getOsAccountLocalIdForUidSync(uid: number): number

Obtains the system account ID based on the process UID. The API returns the result synchronously.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | Process UID. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | System account ID obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300002 | Invalid uid. |

**Example**: Obtain the ID of the system account whose process UID is **12345678**.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
try {
  let localId : number = accountManager.getOsAccountLocalIdForUidSync(uid);
  console.info('getOsAccountLocalIdForUidSync successfully, localId: ' + localId);
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalIdForUidSync exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalIdForDomain9+

getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void

Obtains the system account ID based on the domain account information. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainInfo | [DomainAccountInfo](#domainaccountinfo8) | Yes | Domain account information. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the ID of the system account associated with the domain account. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid domainInfo. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalIdForDomain(domainInfo, (err: BusinessError, localId: number) => {
    if (err) {
      console.error(\`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalIdForDomain9+

getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>

Obtains the system account ID based on the domain account information. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainInfo | [DomainAccountInfo](#domainaccountinfo8) | Yes | Domain account information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the ID of the system account associated with the domain account. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid domainInfo. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
try {
  accountManager.getOsAccountLocalIdForDomain(domainInfo).then((localId: number) => {
    console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(\`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountConstraints(deprecated)

getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void

Obtains all constraints enabled for a system account. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/lJc1X2d0QIam6R8KwN-Mwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BC338B3412E79C4C7545FACD8CBCBD33815E63D70EB4539C6A0395D885B087C)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is all [constraints](#constraints) obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**: Obtain all constraints of system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getOsAccountConstraints(localId, (err: BusinessError, constraints: string\[\]) => {
    if (err) {
      console.error(\`getOsAccountConstraints failed, err: code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('getOsAccountConstraints successfully, constraints: ' + JSON.stringify(constraints));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountConstraints exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountConstraints(deprecated)

getOsAccountConstraints(localId: number): Promise<Array<string>>

Obtains all constraints enabled for a system account. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/CmFsuAE_TdurvSOirlzXcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F04C44B800A579D527177B0E239EC1FC7692D4AF35C0169C8F8EC903AC4705A5)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return all the [constraints](#constraints) enabled for the system account. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**: Obtain all constraints of system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getOsAccountConstraints(localId).then((constraints: string\[\]) => {
    console.info('getOsAccountConstraints, constraints: ' + constraints);
  }).catch((err: BusinessError) => {
    console.error(\`getOsAccountConstraints err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountConstraints exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getActivatedOsAccountLocalIds9+

getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<number>>): void

Obtains information about all activated system accounts. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is a list of activated system accounts. Otherwise, **data** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getActivatedOsAccountLocalIds((err: BusinessError, idArray: number\[\])=>{
    if (err) {
      console.error(\`getActivatedOsAccountLocalIds code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('getActivatedOsAccountLocalIds idArray length:' + idArray.length);
      for(let i=0;i<idArray.length;i++) {
        console.info('activated os account id: ' + idArray\[i\]);
      }
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getActivatedOsAccountLocalIds9+

getActivatedOsAccountLocalIds(): Promise<Array<number>>

Obtains information about all activated system accounts. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the information about all activated system accounts. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getActivatedOsAccountLocalIds().then((idArray: number\[\]) => {
    console.info('getActivatedOsAccountLocalIds, idArray: ' + idArray);
  }).catch((err: BusinessError) => {
    console.error(\`getActivatedOsAccountLocalIds err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getCurrentOsAccount(deprecated)

getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void

Obtains information about the system account to which the current process belongs. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/kyz0Mn6eT8aoH9JpaTZmJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F41A268919BD1A7E69B4C5633DD80B7DAC31BEF41E73C5530B6DB1523AAE7EBE)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.GET\_LOCAL\_ACCOUNTS10+ (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[OsAccountInfo](#osaccountinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account information obtained. Otherwise, **data** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
    if (err) {
      console.error(\`getCurrentOsAccount code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('getCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getCurrentOsAccount(deprecated)

getCurrentOsAccount(): Promise<OsAccountInfo>

Obtains information about the system account to which the current process belongs. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/QWdm_vj-S1qPxNXZfCm94A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4F2EB7A0C8A164D6F3AFA26BF4157CAC009F73B5E70F0CF30859BFE006D766B)

This API is supported since API version 9 and deprecated since API version 11. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.GET\_LOCAL\_ACCOUNTS10+ (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[OsAccountInfo](#osaccountinfo)\> | Promise used to return the system account information obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
    console.info('getCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
  }).catch((err: BusinessError) => {
    console.error(\`getCurrentOsAccount err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountType9+

getOsAccountType(callback: AsyncCallback<OsAccountType>): void

Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[OsAccountType](#osaccounttype)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account type obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountType((err: BusinessError, accountType: osAccount.OsAccountType) => {
    if (err) {
      console.error(\`getOsAccountType err: code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('getOsAccountType accountType: ' + accountType);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountType exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountType9+

getOsAccountType(): Promise<OsAccountType>

Obtains the type of the account to which the current process belongs. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[OsAccountType](#osaccounttype)\> | Promise used to return the system account type obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountType().then((accountType: osAccount.OsAccountType) => {
    console.info('getOsAccountType, accountType: ' + accountType);
  }).catch((err: BusinessError) => {
    console.error(\`getOsAccountType err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountType exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]queryDistributedVirtualDeviceId9+

queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void

Queries the ID of a distributed virtual device. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications) or ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the distributed virtual device ID obtained. Otherwise, **data** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
    if (err) {
      console.error(\`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('queryDistributedVirtualDeviceId virtualID: ' + virtualID);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]queryDistributedVirtualDeviceId9+

queryDistributedVirtualDeviceId(): Promise<string>

Queries the ID of this distributed virtual device. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications) or ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the distributed virtual device ID obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryDistributedVirtualDeviceId().then((virtualID: string) => {
    console.info('queryDistributedVirtualDeviceId, virtualID: ' + virtualID);
  }).catch((err: BusinessError) => {
    console.error(\`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalIdForSerialNumber9+

getOsAccountLocalIdForSerialNumber(serialNumber: number, callback: AsyncCallback<number>): void

Obtains the system account ID based on the SN. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serialNumber | number | Yes | Account SN. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account ID obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid serialNumber. |
| 12300003 | The account indicated by serialNumber does not exist. |

**Example**: Obtain the ID of the system account whose SN is 12345.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
try {
  accountManager.getOsAccountLocalIdForSerialNumber(serialNumber, (err: BusinessError, localId: number)=>{
    if (err) {
      console.error(\`get localId code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('get localId:' + localId + ' by serialNumber: ' + serialNumber);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`get localId exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountLocalIdForSerialNumber9+

getOsAccountLocalIdForSerialNumber(serialNumber: number): Promise<number>

Obtains the system account ID based on the SN. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serialNumber | number | Yes | Account SN. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the system account ID obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid serialNumber. |
| 12300003 | The account indicated by serialNumber does not exist. |

**Example**: Obtain the ID of the system account whose SN is 12345.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
try {
  accountManager.getOsAccountLocalIdForSerialNumber(serialNumber).then((localId: number) => {
    console.info('getOsAccountLocalIdForSerialNumber localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(\`getOsAccountLocalIdForSerialNumber err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountLocalIdForSerialNumber exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getSerialNumberForOsAccountLocalId9+

getSerialNumberForOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void

Obtains the SN of a system account based on the account ID. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the SN obtained. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**: Obtain the SN of the system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getSerialNumberForOsAccountLocalId(localId, (err: BusinessError, serialNumber: number)=>{
    if (err) {
      console.error(\`get serialNumber code is ${err.code}, message is ${err.message}\`);
    } else {
      console.info('get serialNumber:' + serialNumber + ' by localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`get serialNumber exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getSerialNumberForOsAccountLocalId9+

getSerialNumberForOsAccountLocalId(localId: number): Promise<number>

Obtains the SN of a system account based on the account ID. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the SN obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid localId. |
| 12300003 | Account not found. |

**Example**: Obtain the SN of the system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getSerialNumberForOsAccountLocalId(localId).then((serialNumber: number) => {
    console.info('getSerialNumberForOsAccountLocalId serialNumber: ' + serialNumber);
  }).catch((err: BusinessError) => {
    console.error(\`getSerialNumberForOsAccountLocalId err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getSerialNumberForOsAccountLocalId exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]isMultiOsAccountEnable(deprecated)

isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void

Checks whether multiple system accounts are supported. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/a9-9SS_1SrGwJnlSC1qNXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71915896ED78AACF05D81FEF65CD8B9B25D646C3A84F57A97252C60DAEA11DF8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [checkMultiOsAccountEnabled](#checkmultiosaccountenabled9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means multiple system accounts are supported; the value **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isMultiOsAccountEnable((err: BusinessError, isEnabled: boolean) => {
  if (err) {
    console.error(\`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
  }
});

#### \[h2\]isMultiOsAccountEnable(deprecated)

isMultiOsAccountEnable(): Promise<boolean>

Checks whether multiple system accounts are supported. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/8la45r17Rn6PtzCi-JGybQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AFA6DC02B4AE97CA6FBEF265DA8D898C5472FB07498DF0F3AC0B12C4B8612E0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [checkMultiOsAccountEnabled](#checkmultiosaccountenabled9-1) instead.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means multiple system accounts are supported; the value **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isMultiOsAccountEnable().then((isEnabled: boolean) => {
  console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
}).catch((err: BusinessError) => {
  console.error(\`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]isOsAccountActived(deprecated)

isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void

Checks whether a system account is activated. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/yvteKeVfRL2th7SfwF5Dag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61683C54D53CB8F2999FABCADD0BC626AFDF2A30B8EFB71A4CC9E98582B34D23)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

**Example**: Check whether system account 100 is activated.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.isOsAccountActived(localId, (err: BusinessError, isActived: boolean) => {
  if (err) {
    console.error(\`isOsAccountActived failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('isOsAccountActived successfully, isActived:' + isActived);
  }
});

#### \[h2\]isOsAccountActived(deprecated)

isOsAccountActived(localId: number): Promise<boolean>

Checks whether a system account is activated. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/PY4cXnJjTE6xOLGLrodNKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC2F9022A212413898AF6BB913867ECD5FFC676BD15A5EFC188FD2B2F6B23E71)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

**Example**: Check whether system account 100 is activated.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.isOsAccountActived(localId).then((isActived: boolean) => {
  console.info('isOsAccountActived successfully, isActived: ' + isActived);
}).catch((err: BusinessError) => {
  console.error(\`isOsAccountActived failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]isOsAccountConstraintEnable(deprecated)

isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void

Checks whether the specified constraint is enabled for a system account. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/zwPv5TJ8TyyAZe30rUIpMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=317F376C6DA17BAD724C011563C2D05F8E44538610AE48D6CFF635BB65D00953)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| constraint | string | Yes | [Constraint](#constraints) to check. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Example**: Check whether system account 100 is forbidden to use Wi-Fi.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
accountManager.isOsAccountConstraintEnable(localId, constraint, (err: BusinessError, isEnabled: boolean) => {
  if (err) {
    console.error(\`isOsAccountConstraintEnable failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('isOsAccountConstraintEnable successfully, isEnabled: ' + isEnabled);
  }
});

#### \[h2\]isOsAccountConstraintEnable(deprecated)

isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>

Checks whether the specified constraint is enabled for a system account. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/gkygH_6wQVW3pr0GcdsrWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D65AED5E821C2B4B8E1831983C747C5B19C13DEE281C08C5FFF88845F088D0A1)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| constraint | string | Yes | [Constraint](#constraints) to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Example**: Check whether system account 100 is forbidden to use Wi-Fi.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
accountManager.isOsAccountConstraintEnable(localId, constraint).then((isEnabled: boolean) => {
  console.info('isOsAccountConstraintEnable successfully, isEnabled: ' + isEnabled);
}).catch((err: BusinessError) => {
  console.error(\`isOsAccountConstraintEnable err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]isTestOsAccount(deprecated)

isTestOsAccount(callback: AsyncCallback<boolean>): void

Checks whether this system account is a test account. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ljgrhAEwQfyupZC2mfdnnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7022BA68F0CF2505F3A420931A8436E87B073094D4C616D6412216C9929B224)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [checkOsAccountTestable](#checkosaccounttestable9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the account is a test account; the value **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isTestOsAccount((err: BusinessError, isTestable: boolean) => {
  if (err) {
    console.error(\`isTestOsAccount failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
  }
});

#### \[h2\]isTestOsAccount(deprecated)

isTestOsAccount(): Promise<boolean>

Checks whether this system account is a test account. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/rnQVy2w9S6C3y0hUUa4M9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA3650E112C791D0C079186E29A1C9B9077A701AFE108CBCFD70F4DE078CA8FC)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [checkOsAccountTestable](#checkosaccounttestable9-1) instead.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the account is a test account; the value **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.isTestOsAccount().then((isTestable: boolean) => {
    console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
  }).catch((err: BusinessError) => {
    console.error(\`isTestOsAccount failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]isOsAccountVerified(deprecated)

isOsAccountVerified(callback: AsyncCallback<boolean>): void

Checks whether a system account has been verified. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/VrhyKzhOTZWZUZaH7Kx45A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14951B00E151E00639BA03C5877336698F1E256DBFA9B2A8B46F4471ABBF5371)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [checkOsAccountVerified](#checkosaccountverifieddeprecated) instead.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the system account has been verified; the value **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isOsAccountVerified((err: BusinessError, isVerified: boolean) => {
  if (err) {
    console.error(\`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
  }
});

#### \[h2\]isOsAccountVerified(deprecated)

isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void

Checks whether a system account has been verified. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/AeE8bVW9TFq55AalHpoJ7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3736803015AECEB18F4F2AE4005E849A34F9DC2AA8B37BB18F47C762637303A6)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the system account has been verified; the value **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.isOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
  if (err) {
    console.error(\`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
  }
});

#### \[h2\]isOsAccountVerified(deprecated)

isOsAccountVerified(localId?: number): Promise<boolean>

Checks whether a system account has been verified. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/JozinbdBTYWgBUtSpgnaPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E8C3968E4516780DA123873A76680F4D718276A149201478043B83AC3DC4E6A)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | No | ID of the target system account. If this parameter is not specified, this API checks whether the current system account has been verified. The default value is **\-1**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the system account has been verified; the value **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isOsAccountVerified().then((isVerified: boolean) => {
  console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
}).catch((err: BusinessError) => {
  console.error(\`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getCreatedOsAccountsCount(deprecated)

getCreatedOsAccountsCount(callback: AsyncCallback<number>): void

Obtains the number of system accounts created. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/LNH1yyIvRLGx-kpjMA0lFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D6E8E431D86E4DEE6C044F88DDF3C64B893CAF820ECF6710AC7EBE3932FAE5B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountCount](#getosaccountcount9) instead.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the number of created system accounts. If the operation fails, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getCreatedOsAccountsCount((err: BusinessError, count: number)=>{
  if (err) {
    console.error(\`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('getCreatedOsAccountsCount successfully, count: ' + count);
  }
});

#### \[h2\]getCreatedOsAccountsCount(deprecated)

getCreatedOsAccountsCount(): Promise<number>

Obtains the number of system accounts created. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/QSPlvxWtSSiimZ4esgNdGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDC76E64087CFC7C0B0C6E585EBA25A6CDD295CA6215383503176F6A4BA82EA9)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountCount](#getosaccountcount9-1) instead.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of created system accounts. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getCreatedOsAccountsCount().then((count: number) => {
  console.info('getCreatedOsAccountsCount successfully, count: ' + count);
}).catch((err: BusinessError) => {
  console.error(\`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getOsAccountLocalIdFromProcess(deprecated)

getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void

Obtains the ID of the system account to which the current process belongs. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/mpULtP_tQAq79fpeDd01Yg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35D08532B8017A86F99A57D92F263239CA7986FB1BD392E324AB15A3E87398F0)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountLocalId](#getosaccountlocalid9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account ID obtained. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromProcess((err: BusinessError, localId: number) => {
  if (err) {
    console.error(\`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('getOsAccountLocalIdFromProcess id:: ' + localId);
  }
});

#### \[h2\]getOsAccountLocalIdFromProcess(deprecated)

getOsAccountLocalIdFromProcess(): Promise<number>

Obtains the ID of the system account to which the current process belongs. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/PTDORhrDRFa2pt_MY4EbRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=071BC3D7BD20704AAFB23329C96B4A49F6E37FED9C2BECD100F2E9C79F40F999)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountLocalId](#getosaccountlocalid9-1) instead.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the system account ID obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromProcess().then((localId: number) => {
  console.info('getOsAccountLocalIdFromProcess successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(\`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getOsAccountLocalIdFromUid(deprecated)

getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void

Obtains the system account ID based on the process UID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/_grfbmPKTteNgUtJ7IvEkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A54233CA25AD3189C9EF53FE7705BEAD14E3C40E3C6A5637C8B1E50B9662DE9)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountLocalIdForUid](#getosaccountlocalidforuid9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | Process UID. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account ID obtained. Otherwise, **data** is an error object. |

**Example**: Obtain the ID of the system account whose process UID is **12345678**.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
accountManager.getOsAccountLocalIdFromUid(uid, (err: BusinessError, localId: number) => {
  if (err) {
    console.error(\`getOsAccountLocalIdFromUid failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('getOsAccountLocalIdFromUid successfully, localId: ' + localId);
  }
});

#### \[h2\]getOsAccountLocalIdFromUid(deprecated)

getOsAccountLocalIdFromUid(uid: number): Promise<number>

Obtains the system account ID based on the process UID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Opmsen0eTHCCYdm3Hi7_-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAC7E2A398E30CF5B829BB98207972A741EAE31E21F68FF66F2D370E24AC119A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountLocalIdForUid](#getosaccountlocalidforuid9-1) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uid | number | Yes | Process UID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the system account ID obtained. |

**Example**: Obtain the ID of the system account whose process UID is **12345678**.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let uid: number = 12345678;
accountManager.getOsAccountLocalIdFromUid(uid).then((localId: number) => {
  console.info('getOsAccountLocalIdFromUid successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(\`getOsAccountLocalIdFromUid failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getOsAccountLocalIdFromDomain(deprecated)

getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void

Obtains the system account ID based on the domain account information. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/0jio_dNYR0Gk0yq5xarJrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=206BFEB6D79E51BB4C447E9B1B64582B921795CD33F16B5B933D5A9465EE2DC8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain9) instead.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainInfo | [DomainAccountInfo](#domainaccountinfo8) | Yes | Domain account information. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account ID obtained. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromDomain(domainInfo, (err: BusinessError, localId: number) => {
  if (err) {
    console.error(\`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
  }
});

#### \[h2\]getOsAccountLocalIdFromDomain(deprecated)

getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>

Obtains the system account ID based on the domain account information. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/88a64suiT6mTS-dACOxLmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC6CCB6E1BBA074D04093FDB01295AA988A8165424BA9BBDE4F0505CED97C1ED)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain9-1) instead.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainInfo | [DomainAccountInfo](#domainaccountinfo8) | Yes | Domain account information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the ID of the system account associated with the domain account. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
accountManager.getOsAccountLocalIdFromDomain(domainInfo).then((localId: number) => {
  console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(\`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getOsAccountAllConstraints(deprecated)

getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void

Obtains all constraints enabled for a system account. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/zqc1EN5UQlOJ1AVVLtULJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D897CFF4E3620260A478009D27D1F197F1DA3A49813DAFD739D9A2CF1B5C4E6)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is a list of all [constraints](#constraints) enabled for the system account. Otherwise, **err** is an error object. |

**Example**: Obtain all constraints of system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getOsAccountAllConstraints(localId, (err: BusinessError, constraints: string\[\])=>{
  if (err) {
    console.error(\`getOsAccountAllConstraints code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('getOsAccountAllConstraints:' + JSON.stringify(constraints));
  }
});

#### \[h2\]getOsAccountAllConstraints(deprecated)

getOsAccountAllConstraints(localId: number): Promise<Array<string>>

Obtains all constraints enabled for a system account. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/AjLXZwgyQhSN1ko5-4CVuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E58A3DB7D791DCCFDAD6718D5E61B0B392439AD8AB4897D785958B31D5F9E5B0)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return all the [constraints](#constraints) enabled for the system account. |

**Example**: Obtain all constraints of system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getOsAccountAllConstraints(localId).then((constraints: string\[\]) => {
  console.info('getOsAccountAllConstraints, constraints: ' + constraints);
}).catch((err: BusinessError) => {
  console.error(\`getOsAccountAllConstraints err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]queryActivatedOsAccountIds(deprecated)

queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void

Obtains information about all activated system accounts. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/CCJLsSeYQCSYzHVOwya9bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DC681E7713A4420E05360092A551C6B1F6251F7B9BF2FB65CAC6559567F28BA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is a list of activated system accounts. Otherwise, **data** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryActivatedOsAccountIds((err: BusinessError, idArray: number\[\]) => {
  if (err) {
    console.error(\`queryActivatedOsAccountIds code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('queryActivatedOsAccountIds idArray length:' + idArray.length);
    for (let i = 0; i < idArray.length; i++) {
      console.info('activated os account id: ' + idArray\[i\]);
    }
  }
});

#### \[h2\]queryActivatedOsAccountIds(deprecated)

queryActivatedOsAccountIds(): Promise<Array<number>>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/tTRvdHAyRneCxVxc-RQjkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BFBB31BE94640597FCA9BFA378C68E59F16300A1FAD7527C2C224BD5E3F06BC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids9-1) instead.

Obtains information about all activated system accounts. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the information about all activated system accounts. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryActivatedOsAccountIds().then((idArray: number\[\]) => {
  console.info('queryActivatedOsAccountIds, idArray: ' + idArray);
}).catch((err: BusinessError) => {
  console.error(\`queryActivatedOsAccountIds err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]queryCurrentOsAccount(deprecated)

queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void

Obtains information about the system account to which the current process belongs. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/7mAIIk9sQwCZyUHskd0XCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68090CE4C57B1F2D2FBF1AFA82E80DAB6869DC04A249D2C7AE28EE3069E258E6)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[OsAccountInfo](#osaccountinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account information obtained. Otherwise, **data** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
  if (err) {
    console.error(\`queryCurrentOsAccount code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('queryCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
  }
});

#### \[h2\]queryCurrentOsAccount(deprecated)

queryCurrentOsAccount(): Promise<OsAccountInfo>

Obtains information about the system account to which the current process belongs. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/gZ_GK6N6R8WuaT81TI0o6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54338848B705B6B5FD34F7F837F87D521FB06BB08CAA27859C0599F177B03C49)

This API is supported since API version 7 and deprecated since API version 9. The substitute API is available only to system applications.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications)

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[OsAccountInfo](#osaccountinfo)\> | Promise used to return the system account information obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
  console.info('queryCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
}).catch((err: BusinessError) => {
  console.error(\`queryCurrentOsAccount err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getOsAccountTypeFromProcess(deprecated)

getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void

Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/3LAmOx0zSImNIPwm6SmEBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E98064D11F50E12ECD34639F6332E7B61AC6A6AA98796483DB2E55307810084C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountType](#getosaccounttype9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[OsAccountType](#osaccounttype)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account type obtained. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountTypeFromProcess((err: BusinessError, accountType: osAccount.OsAccountType) => {
  if (err) {
    console.error(\`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('getOsAccountTypeFromProcess accountType: ' + accountType);
  }
});

#### \[h2\]getOsAccountTypeFromProcess(deprecated)

getOsAccountTypeFromProcess(): Promise<OsAccountType>

Obtains the type of the account to which the current process belongs. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/kvkYUIAzSgiNqDlE7_lslg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDDCCE99ED64A9E116C1AA14DB0A26E1A86F3998B26506FC3D25984120792C29)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [getOsAccountType](#getosaccounttype9-1) instead.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[OsAccountType](#osaccounttype)\> | Promise used to return the system account type obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountTypeFromProcess().then((accountType: osAccount.OsAccountType) => {
  console.info('getOsAccountTypeFromProcess, accountType: ' + accountType);
}).catch((err: BusinessError) => {
  console.error(\`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getDistributedVirtualDeviceId(deprecated)

getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void

Obtains the ID of a distributed virtual device. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/yM1yRntJQQiSfpRPhldQbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE4E59951601832C0EABC11F1269774352B536C3FC2E7866607D7567C4656998)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid9) instead.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications) or ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the distributed virtual device ID obtained. Otherwise, **data** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
  if (err) {
    console.error(\`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('getDistributedVirtualDeviceId virtualID: ' + virtualID);
  }
});

#### \[h2\]getDistributedVirtualDeviceId(deprecated)

getDistributedVirtualDeviceId(): Promise<string>

Obtains the ID of this distributed virtual device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/O_2iJv0URU6kiHsTcT3XEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3E52AD32DD1E455142D97264A533398DE62999A5E1F9AECDD2962F27BB73C2B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid9-1) instead.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS (available only for system applications) or ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the distributed virtual device ID obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getDistributedVirtualDeviceId().then((virtualID: string) => {
  console.info('getDistributedVirtualDeviceId, virtualID: ' + virtualID);
}).catch((err: BusinessError) => {
  console.error(\`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getOsAccountLocalIdBySerialNumber(deprecated)

getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void

Obtains the system account ID based on the SN. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/mMz_dmDFRLuZL7lhBX5Iog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA0A1C540072961450A3E357DDCF53C858CD632E58EBCCDEB320C8C8F642CD83)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serialNumber | number | Yes | Account SN. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the system account ID obtained. Otherwise, **err** is an error object. |

**Example**: Obtain the ID of the system account whose SN is 12345.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
accountManager.getOsAccountLocalIdBySerialNumber(serialNumber, (err: BusinessError, localId: number)=>{
  if (err) {
    console.error(\`get localId code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('get localId:' + localId + ' by serialNumber: ' + serialNumber);
  }
});

#### \[h2\]getOsAccountLocalIdBySerialNumber(deprecated)

getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>

Obtains the system account ID based on the SN. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/6Mtm58xJR7qocL6pP26hpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=380102CC1B8584161E9C13EEAE58180BF1E80EB5907502FE321091E9D3FA72F2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber9-1) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| serialNumber | number | Yes | Account SN. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the system account ID obtained. |

**Example**: Obtain the ID of the system account whose SN is 12345.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let serialNumber: number = 12345;
accountManager.getOsAccountLocalIdBySerialNumber(serialNumber).then((localId: number) => {
  console.info('getOsAccountLocalIdBySerialNumber localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(\`getOsAccountLocalIdBySerialNumber err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getSerialNumberByOsAccountLocalId(deprecated)

getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void

Obtains the SN of a system account based on the account ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/ktKsMo1KSmmhTN4QQI0BpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5887D3D4FD2C25DFC7D24ABDFA2CF7B86A3EF8F61EB7B3164C037A550203DA3F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid9) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the SN obtained. Otherwise, **err** is an error object. |

**Example**: Obtain the SN of the system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getSerialNumberByOsAccountLocalId(localId, (err: BusinessError, serialNumber: number)=>{
  if (err) {
    console.error(\`get serialNumber code is ${err.code}, message is ${err.message}\`);
  } else {
    console.info('get serialNumber:' + serialNumber + ' by localId: ' + localId);
  }
});

#### \[h2\]getSerialNumberByOsAccountLocalId(deprecated)

getSerialNumberByOsAccountLocalId(localId: number): Promise<number>

Obtains the SN of a system account based on the account ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/ruG_UM5YSjaF6IEDEHnfig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFBDEE001F4A9D5E77D250742870372AE69D15BCBA55C08127F4B3C3E63C6799)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid9-1) instead.

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the SN obtained. |

**Example**: Obtain the SN of the system account 100.

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getSerialNumberByOsAccountLocalId(localId).then((serialNumber: number) => {
  console.info('getSerialNumberByOsAccountLocalId serialNumber: ' + serialNumber);
}).catch((err: BusinessError) => {
  console.error(\`getSerialNumberByOsAccountLocalId err: code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getOsAccountName12+

getOsAccountName(): Promise<string>

Obtains the name of the system account of the caller. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the system account name obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountName().then((name: string) => {
    console.info('getOsAccountName, name: ' + name);
  }).catch((err: BusinessError) => {
    console.error('getOsAccountName err: ' + err);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getOsAccountName exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getForegroundOsAccountLocalId15+

getForegroundOsAccountLocalId(): Promise<number>

Obtains the ID of the foreground system account. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getForegroundOsAccountLocalId().then((localId: number) => {
    console.info('getForegroundOsAccountLocalId, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(\`getForegroundOsAccountLocalId err: code is ${err.code}, message is ${err.message}\`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`getForegroundOsAccountLocalId exception: code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getOsAccountDomainInfo15+

getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>

Obtains the domain account information associated with a specified system account. This API uses a promise to return the result.

**Required permissions**: ohos.permission.GET\_DOMAIN\_ACCOUNTS and ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS (available to system applications and enterprise applications)

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localId | number | Yes | ID of the target system account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DomainAccountInfo](#domainaccountinfo8)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 12300001 | The system service works abnormally. |
| 12300003 | OS account not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getOsAccountDomainInfo(localId).then((domainAccountInfo: osAccount.DomainAccountInfo) => {
  if (domainAccountInfo === null) {
    console.info('The target OS account is not a domain account.')
  } else {
    console.info('getOsAccountDomainInfo domain: ' + domainAccountInfo.domain);
    console.info('getOsAccountDomainInfo accountName: ' + domainAccountInfo.accountName);
  }
}).catch((err: BusinessError) => {
  console.error(\`getOsAccountDomainInfo err: code is ${err.code}, message is ${err.message}\`);
})

#### DomainAccountManager18+

Provides APIs for domain account management.

#### \[h2\]updateAccountInfo18+

updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>

Updates information of a domain account. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_LOCAL\_ACCOUNTS or ohos.permission.MANAGE\_DOMAIN\_ACCOUNTS

**System capability**: SystemCapability.Account.OsAccount

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldAccountInfo | [DomainAccountInfo](#domainaccountinfo8) | Yes | Domain account information. |
| newAccountInfo | [DomainAccountInfo](#domainaccountinfo8) | Yes | New domain account information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | The new account info is invalid. |
| 12300003 | The old account not found. |
| 12300004 | The new account already exists. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let oldDomainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'oldtestAccountName'};
let newDomainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'newtestAccountName'};
try {
  osAccount.DomainAccountManager.updateAccountInfo(oldDomainInfo, newDomainInfo).then(() => {
    console.info('updateAccountInfo, success');
  }).catch((err: BusinessError) => {
    console.error('updateAccountInfo err: ' + err);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(\`updateAccountInfo exception: code is ${err.code}, message is ${err.message}\`);
}

#### OsAccountInfo

Represents information about a system account.

**System capability**: SystemCapability.Account.OsAccount

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| localId | number | No | No | ID of the target system account. |
| localName | string | No | No | Name of the system account. |
| type | [OsAccountType](#osaccounttype) | No | No | Type of the system account. |
| constraints | Array<string> | No | No | [Constraints](#constraints) of the system account. By default, no value is passed in. |
| isVerified(deprecated) | boolean | No | No | 
Whether the account has been verified. The value **true** means the specified account has been verified; the value **false** means the opposite.

Note: This parameter is supported since API version 7 and deprecated since API version 11. You are advised to use **isUnlocked** instead.

 |
| isUnlocked11+ | boolean | No | No | Whether the account is unlocked (whether the **el2/** directory is decrypted). The value **true** means the specified account is unlocked; the value **false** means the opposite. |
| photo8+ | string | No | No | Avatar of the system account. By default, no value is passed in. |
| createTime8+ | number | No | No | Time when the system account was created. |
| lastLoginTime8+ | number | No | No | Last login time of the system account. By default, no value is passed in. |
| serialNumber8+ | number | No | No | SN of the system account. |
| isActived(deprecated) | boolean | No | No | 

Whether the system account is activated. The value **true** means the specified account is activated; the value **false** means the opposite.

Note: This parameter is supported since API version 7 and deprecated since API version 11. You are advised to use **isActivated** instead.

 |
| isActivated11+ | boolean | No | No | Whether the system account is activated. The value **true** means the specified account is activated; the value **false** means the opposite. |
| isCreateCompleted8+ | boolean | No | No | Whether the system account information is complete. The value **true** means the specified account is complete; the value **false** means the opposite. |
| distributedInfo | [distributedAccount.DistributedInfo](../ohos-account-distributedaccount-distributed-account-management/document.md#distributedinfo) | No | No | Distributed account information. By default, no value is passed in. |
| domainInfo8+ | [DomainAccountInfo](#domainaccountinfo8) | No | No | Domain account information. By default, no value is passed in. |

#### DomainAccountInfo8+

Represents the domain account information.

**System capability**: SystemCapability.Account.OsAccount

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| domain | string | No | No | Domain name. |
| accountName | string | No | No | Domain account name. |
| serverConfigId18+ | string | No | Yes | Domain account configuration ID, which is an empty string by default. |

#### DomainServerConfig18+

Represents the configuration of a domain server.

**System capability**: SystemCapability.Account.OsAccount

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| parameters | Record<string, Object> | No | No | Server configuration parameters. |
| id | string | No | No | Server configuration ID. |
| domain | string | No | No | Domain to which the server belongs. |

#### DomainServerConfigManager18+

Provides APIs for domain server configuration and management.

#### \[h2\]addServerConfig18+

static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>

Adds domain server configuration. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Required permissions**: ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parameters | Record<string, Object> | Yes | Configuration parameters of the domain server. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DomainServerConfig](#domainserverconfig18)\> | Promise used to return the configuration of the newly added domain server. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid server config parameters. |
| 12300211 | Server unreachable. |
| 12300213 | Server config already exists. |
| 12300215 | The number of server config reaches the upper limit. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
}).catch((err: BusinessError) => {
  console.error(\`add server configuration failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]removeServerConfig18+

static removeServerConfig(configId: string): Promise<void>

Removes domain server configuration. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Required permissions**: ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configId | string | Yes | Server configuration ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300212 | Server config not found. |
| 12300214 | Server config has been associated with an account. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.removeServerConfig(serverConfig.id);
  console.info('remove domain server configuration successfully');
}).catch((err: BusinessError) => {
  console.error(\`add server configuration failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]updateServerConfig18+

static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>

Updates the domain server configuration. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Required permissions**: ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configId | string | Yes | Server configuration ID. |
| parameters | Record<string, Object> | Yes | Configuration parameters of the domain server. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DomainServerConfig](#domainserverconfig18)\> | Promise used to return the updated domain server configuration. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300002 | Invalid server config parameters. |
| 12300211 | Server unreachable. |
| 12300212 | Server config not found. |
| 12300213 | Server config already exists. |
| 12300214 | Server config has been associated with an account. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.updateServerConfig(serverConfig.id, configParams).then((data) => {
    console.info('update domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(\`update domain server configuration failed, code is ${err.code}, message is ${err.message}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`add server configuration failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getServerConfig18+

static getServerConfig(configId: string): Promise<DomainServerConfig>

Obtains the domain server configuration. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Required permissions**: ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configId | string | Yes | Server configuration ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DomainServerConfig](#domainserverconfig18)\> | Promise used to return the domain server configuration obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300212 | Server config not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.getServerConfig(serverConfig.id).then((data: osAccount.DomainServerConfig) => {
    console.info('get domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(\`get domain server configuration failed, code is ${err.code}, message is ${err.message}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`add server configuration failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getAllServerConfigs18+

static getAllServerConfigs(): Promise<Array<DomainServerConfig>>

Obtains the configurations of all domain servers. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Required permissions**: ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[DomainServerConfig](#domainserverconfig18)\>> | Promise used to return the domain server configuration obtained. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.getAllServerConfigs().then((data: Array<osAccount.DomainServerConfig>) => {
    console.info('get all domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(\`get all domain server configuration failed, code is ${err.code}, message is ${err.message}\`);
  });
}).catch((err: BusinessError) => {
  console.error(\`add server configuration failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getAccountServerConfig18+

static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>

Obtains the server configuration of a domain account. This API uses a promise to return the result.

**System capability**: SystemCapability.Account.OsAccount

**Required permissions**: ohos.permission.MANAGE\_DOMAIN\_ACCOUNT\_SERVER\_CONFIGS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| domainAccountInfo | [DomainAccountInfo](#domainaccountinfo8) | Yes | Information of the domain account. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DomainServerConfig](#domainserverconfig18)\> | Promise used to return the domain server configuration of the account. |

**Error codes**

For details about the error codes, see [Account Management Error Codes](../../../error-codes/account-management-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 12300001 | The system service works abnormally. |
| 12300003 | Domain account not found. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let accountInfo: osAccount.DomainAccountInfo = {
  'accountName': 'demoName',
  'domain': 'demoDomain'
};
osAccount.DomainServerConfigManager.getAccountServerConfig(accountInfo).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('get account server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
}).catch((err: BusinessError) => {
  console.error(\`add server configuration failed, code is ${err.code}, message is ${err.message}\`);
});

#### Constraints

| Constraint | Description |
| :-- | :-- |
| constraint.wifi | Disallow the use of Wi-Fi. |
| constraint.wifi.set | Disallow setting of Wi-Fi. |
| constraint.locale.set | Disallow setting of the language to use. |
| constraint.app.accounts | Disallow addition or deletion of application accounts. |
| constraint.apps.install | Disallow application installation. |
| constraint.apps.uninstall | Disallow application uninstallation. |
| constraint.location.shared | Disallow location sharing. |
| constraint.unknown.sources.install | Disallow installation of apps from unknown sources. |
| constraint.global.unknown.app.install | Disallow installation of apps from unknown sources for all users. |
| constraint.bluetooth.set | Disallow setting of Bluetooth. |
| constraint.bluetooth | Disallow the use of Bluetooth. |
| constraint.bluetooth.share | Disallow Bluetooth sharing. |
| constraint.usb.file.transfer | Disallow file transfer over USB. |
| constraint.credentials.set | Disallow setting of user credentials. |
| constraint.os.account.remove | Disallow removal of users. |
| constraint.managed.profile.remove | Disallow removal of the managed profiles of this user. |
| constraint.debug.features.use | Disallow the use of debugging features. |
| constraint.vpn.set | Disallow setting of VPN. |
| constraint.date.time.set | Disallow setting of date, time, or time zone. |
| constraint.tethering.config | Disallow setting of Tethering. |
| constraint.network.reset | Disallow reset of network settings. |
| constraint.factory.reset | Disallow reset to factory settings. |
| constraint.os.account.create | Disallow creation of new users. |
| constraint.add.managed.profile | Disallow addition of managed profiles. |
| constraint.apps.verify.disable | Disallow application verification from being disabled. |
| constraint.cell.broadcasts.set | Disallow setting of cell broadcasts. |
| constraint.mobile.networks.set | Disallow setting of mobile networks. |
| constraint.control.apps | Disallow modification of apps in **Settings** or the boot module. |
| constraint.physical.media | Disallow mounting of external physical media. |
| constraint.microphone | Disallow the use of microphones. |
| constraint.microphone.unmute | Disallow unmuting of the microphone. |
| constraint.volume.adjust | Disallow adjustment of the volume. |
| constraint.calls.outgoing | Disallow outgoing calls. |
| constraint.sms.use | Disallow the use of the short message service (SMS). |
| constraint.fun | Disallow the use of entertainment features. |
| constraint.windows.create | Disallow creation of the windows other than application windows. |
| constraint.system.error.dialogs | Disallow display of error dialogs for crashed or unresponsive apps. |
| constraint.cross.profile.copy.paste | Disallow pasting of clipboard content to other users or profiles. |
| constraint.beam.outgoing | Disallow the use of Near Field Communications (NFC) to transfer data from apps. |
| constraint.wallpaper | Disallow wallpaper management. |
| constraint.safe.boot | Disallow reboot of the device in safe boot mode. |
| constraint.parent.profile.app.linking | Disallow the application in the parent profile from handling web links from the managed profiles. |
| constraint.audio.record | Disallow audio recording. |
| constraint.camera.use | Disallow the use of cameras. |
| constraint.os.account.background.run | Disallow background system accounts. |
| constraint.data.roam | Disallow the use of cellular data when roaming. |
| constraint.os.account.set.icon | Disallow setting of user icons. |
| constraint.wallpaper.set | Disallow setting of wallpapers. |
| constraint.oem.unlock | Disallow the use of OEM unlock. |
| constraint.device.unmute | Disallow unmuting of the device. |
| constraint.password.unified | Disallow the use of the unified lock screen challenge for the managed profile with the primary user. |
| constraint.autofill | Disallow the use of the autofill service. |
| constraint.content.capture | Disallow capturing of the screen content. |
| constraint.content.suggestions | Disallow receiving of content suggestions. |
| constraint.os.account.activate | Disallow activating of system accounts in the foreground. |
| constraint.location.set | Disallow setting of the location service. |
| constraint.airplane.mode.set | Disallow setting of the airplane mode. |
| constraint.brightness.set | Disallow setting of the brightness. |
| constraint.share.into.profile | Disallow sharing of files, images, and data of the primary user to the managed profiles. |
| constraint.ambient.display | Disallow display of the ambient environment. |
| constraint.screen.timeout.set | Disallow setting of the screen-off timeout. |
| constraint.print | Disallow printing. |
| constraint.private.dns.set | Disallow setting of the private domain name server (DNS). |
