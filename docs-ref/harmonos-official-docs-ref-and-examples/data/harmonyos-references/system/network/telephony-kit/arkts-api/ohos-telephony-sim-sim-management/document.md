# @ohos.telephony.sim (SIM Management)

The **sim** module provides basic SIM card management functions. With the APIs provided by this module, you can obtain the ISO country code, home PLMN ID, service provider name, SIM card status, type, installation status, and activation status of the SIM card in the specified slot.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/AHiMQxIKTFWFTQjCQWqoKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB145AF3E86A30CCACB219F58CB4AA82A015DBE4AA488399575AF75802C85C45)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { sim } from '@kit.TelephonyKit';

#### sim.isSimActive7+

isSimActive(slotId: number, callback: AsyncCallback<boolean>): void

Checks whether the SIM card in the specified slot is activated. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<boolean> | Yes | 

Callback used to return the result, which indicates whether the SIM card in the specified slot is activated.

**true**: activated.

**false**: not activated.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0, (err: BusinessError, data: boolean) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.isSimActive7+

isSimActive(slotId: number): Promise<boolean>

Checks whether the SIM card in the specified slot is activated. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the result.

**true**: activated.

**false**: not activated.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0).then((data: boolean) => {
    console.info(\`isSimActive success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`isSimActive failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.isSimActiveSync10+

isSimActiveSync(slotId: number): boolean

Checks whether the SIM card in the specified slot is activated.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the SIM card in the specified slot is activated.

**true**: activated.

**false**: not activated.

 |

**Example**

import { sim } from '@kit.TelephonyKit';

let isSimActive: boolean = sim.isSimActiveSync(0);
console.info(\`the sim is active:\` + isSimActive);

#### sim.getDefaultVoiceSlotId7+

getDefaultVoiceSlotId(callback: AsyncCallback<number>): void

Obtains the default slot ID of the SIM card that provides voice services. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | 
Callback used to return the result.

\- **0**: card slot 1.

\- **1**: card slot 2.

\- **\-1**: card slot not set or service not unavailable

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSlotId((err: BusinessError, data: number) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getDefaultVoiceSlotId7+

getDefaultVoiceSlotId(): Promise<number>

Obtains the default slot ID of the SIM card that provides voice services. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | 
Promise used to return the result.

\- **0**: card slot 1.

\- **1**: card slot 2.

\- **\-1**: card slot not set or service not unavailable

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSlotId().then((data: number) => {
    console.info(\`getDefaultVoiceSlotId success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getDefaultVoiceSlotId failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.hasOperatorPrivileges7+

hasOperatorPrivileges(slotId: number, callback: AsyncCallback<boolean>): void

Checks whether the application (caller) has been granted the operator permission. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<boolean> | Yes | 

Callback used to return the result, which indicates whether the application (caller) has been granted the operator permission.

\- **true**: The application (caller) has been granted the operator permission.

**false**: The application (caller) has not been granted the operator permission.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasOperatorPrivileges(0, (err: BusinessError, data: boolean) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.hasOperatorPrivileges7+

hasOperatorPrivileges(slotId: number): Promise<boolean>

Checks whether the application (caller) has been granted the operator permission. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the application (caller) has been granted the carrier permission, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasOperatorPrivileges(0).then((data: boolean) => {
    console.info(\`hasOperatorPrivileges success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`hasOperatorPrivileges failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getISOCountryCodeForSim

getISOCountryCodeForSim(slotId: number, callback: AsyncCallback<string>): void

Obtains the ISO country code of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the result, which is a country code, for example, **CN** (China). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getISOCountryCodeForSim(0, (err: BusinessError, data: string) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getISOCountryCodeForSim

getISOCountryCodeForSim(slotId: number): Promise<string>

Obtains the ISO country code of the SIM card in the specified slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result, which is the ISO country code of the SIM card in the specified slot, for example, **CN** (China). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getISOCountryCodeForSim(0).then((data: string) => {
    console.info(\`getISOCountryCodeForSim success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getISOCountryCodeForSim failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getISOCountryCodeForSimSync10+

getISOCountryCodeForSimSync(slotId: number): string

Obtains the ISO country code of the SIM card in the specified slot.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | ISO country code of the SIM card in the specified slot, for example, **CN** (China). |

**Example**

import { sim } from '@kit.TelephonyKit';

let countryCode: string = sim.getISOCountryCodeForSimSync(0);
console.info(\`the country ISO is:\` + countryCode);

#### sim.getSimOperatorNumeric

getSimOperatorNumeric(slotId: number, callback: AsyncCallback<string>): void

Obtains the home public land mobile network (PLMN) ID of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the result, which is the home PLMN ID of the SIM card in the specified slot. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0, (err: BusinessError, data: string) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getSimOperatorNumeric

getSimOperatorNumeric(slotId: number): Promise<string>

Obtains the home PLMN ID of the SIM card in the specified slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0).then((data: string) => {
    console.info(\`getSimOperatorNumeric success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getSimOperatorNumeric failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getSimOperatorNumericSync10+

getSimOperatorNumericSync(slotId: number): string

Obtains the home PLMN ID of the SIM card in the specified slot. This API returns the result synchronously.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Home PLMN ID of the SIM card in the specified slot. |

**Example**

import { sim } from '@kit.TelephonyKit';

let numeric: string = sim.getSimOperatorNumericSync(0);
console.info(\`the sim operator numeric is:\` + numeric);

#### sim.getSimSpn

getSimSpn(slotId: number, callback: AsyncCallback<string>): void

Obtains the service provider name (SPN) of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the result, which is the SPN of the SIM card in the specified slot. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimSpn(0, (err: BusinessError, data: string) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getSimSpn

getSimSpn(slotId: number): Promise<string>

Obtains the SPN of the SIM card in the specified slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimSpn(0).then((data: string) => {
    console.info(\`getSimSpn success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getSimSpn failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getSimSpnSync10+

getSimSpnSync(slotId: number): string

Obtains the SPN of the SIM card in the specified slot. This API returns the result synchronously.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | SPN of the SIM card in the specified slot. |

**Example**

import { sim } from '@kit.TelephonyKit';

let spn: string = sim.getSimSpnSync(0);
console.info(\`the sim card spn is:\` + spn);

#### sim.getSimState

getSimState(slotId: number, callback: AsyncCallback<SimState>): void

Obtains the state of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<[SimState](#simstate)\> | Yes | Callback used to return the result, which is the state of the SIM card in the specified slot. For details, see [SimState](#simstate). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0, (err: BusinessError, data: sim.SimState) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getSimState

getSimState(slotId: number): Promise<SimState>

Obtains the state of the SIM card in the specified slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SimState](#simstate)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0).then((data: sim.SimState) => {
    console.info(\`getSimState success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getSimState failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getSimStateSync10+

getSimStateSync(slotId: number): SimState

Obtains the state of the SIM card in the specified slot.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimState](#simstate) | State of the SIM card in the specified slot. |

**Example**

import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(\`The sim state is:\` + simState);

#### sim.getCardType7+

getCardType(slotId: number, callback: AsyncCallback<CardType>): void

Obtains the type of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<[CardType](#cardtype7)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getCardType(0, (err: BusinessError, data: sim.CardType) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getCardType7+

getCardType(slotId: number): Promise<CardType>

Obtains the type of the SIM card in the specified slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[CardType](#cardtype7)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getCardType(0).then((data: sim.CardType) => {
    console.info(\`getCardType success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getCardType failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getCardTypeSync10+

getCardTypeSync(slotId: number): CardType

Obtains the type of the SIM card in the specified slot.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [CardType](#cardtype7) | Type of the SIM card in the specified slot. |

**Example**

import { sim } from '@kit.TelephonyKit';

let cardType: sim.CardType = sim.getCardTypeSync(0);
console.info(\`the card type is:\` + cardType);

#### sim.hasSimCard7+

hasSimCard(slotId: number, callback: AsyncCallback<boolean>): void

Checks whether the SIM card in the specified slot is installed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<boolean> | Yes | 

Callback used to return the result.

\- **true**: installed.

\- **false**: not installed.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasSimCard(0, (err: BusinessError, data: boolean) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.hasSimCard7+

hasSimCard(slotId: number): Promise<boolean>

Checks whether the SIM card in the specified slot is installed. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the result.

\- **true**: installed.

\- **false**: not installed.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasSimCard(0).then((data: boolean) => {
    console.info(\`hasSimCard success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`hasSimCard failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.hasSimCardSync10+

hasSimCardSync(slotId: number): boolean

Checks whether the SIM card in the specified slot is installed.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the SIM card in the specified slot is installed.

\- **true**: installed.

\- **false**: not installed.

 |

**Example**

import { sim } from '@kit.TelephonyKit';

let hasSimCard: boolean = sim.hasSimCardSync(0);
console.info(\`has sim card: \` + hasSimCard);

#### sim.getSimAccountInfo10+

getSimAccountInfo(slotId: number, callback: AsyncCallback<IccAccountInfo>): void

Obtains SIM card account information. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_TELEPHONY\_STATE

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/vxc3K6g8R1WMqkzELiXnzQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8455CB170D152EB4346FD2E5A89A166A6633D9FF63A66AFF5EBCADA3366A713B)

The **GET\_TELEPHONY\_STATE** permission is required to obtain the ICCID and phone number. Such information is sensitive and not open to third-party applications. When this API is called, the returned ICCID and phone number are empty.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<[IccAccountInfo](#iccaccountinfo10)\> | Yes | Callback used to return the result, which is the account information of the SIM card in the specified slot. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301002 | The SIM card failed to read or update data. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0, (err:BusinessError , data: sim.IccAccountInfo) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getSimAccountInfo10+

getSimAccountInfo(slotId: number): Promise<IccAccountInfo>

Obtains SIM card account information. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_TELEPHONY\_STATE

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Riu22g3HRLOACEl8Z-JRLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFFBBBD26FADBBC1EC5025BEB2B2BDFB0F478E13FCA6E78DE80A2B2D9205E9A8)

The **GET\_TELEPHONY\_STATE** permission is required to obtain the ICCID and phone number. Such information is sensitive and not open to third-party applications. When this API is called, the returned ICCID and phone number are empty.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[IccAccountInfo](#iccaccountinfo10)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301002 | The SIM card failed to read or update data. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0).then((data: sim.IccAccountInfo) => {
    console.info(\`getSimAccountInfo success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getSimAccountInfo failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getActiveSimAccountInfoList10+

getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void

Obtains the list of activated SIM card accounts. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_TELEPHONY\_STATE

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/vzrwgQxHRlm1IS7iqlhfDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C5B4625D54FCB88F37CB2C2BAAED2B7D03F28C01A1F5FE847C72BF2FFE941F7)

The **GET\_TELEPHONY\_STATE** permission is required to obtain the ICCID and phone number. Such information is sensitive and not open to third-party applications. When this API is called, the returned ICCID and phone number are empty.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[IccAccountInfo](#iccaccountinfo10)\>> | Yes | Callback used to return the result, which is a list of activated SIM card accounts. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList((err: BusinessError, data: Array<sim.IccAccountInfo>) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getMaxSimCount7+

getMaxSimCount(): number

Obtains the number of card slots.

**System capability**: SystemCapability.Telephony.CoreService

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of card slots. |

**Example**

import { sim } from '@kit.TelephonyKit';

console.info("Result: "+ sim.getMaxSimCount());

#### sim.getActiveSimAccountInfoList10+

getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>

Obtains the list of activated SIM card accounts. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_TELEPHONY\_STATE

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/faKCwTHAS2mpd0nZUedv5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6F2C11111C80AE6FF8510C5DD1D9D126023F22C5028B2021D76ED8E229C018F)

The **GET\_TELEPHONY\_STATE** permission is required to obtain the ICCID and phone number. Such information is sensitive and not open to third-party applications. When this API is called, the returned ICCID and phone number are empty.

**System capability**: SystemCapability.Telephony.CoreService

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[IccAccountInfo](#iccaccountinfo10)\>> | Promise used to return the result. |

**Error codes**

For details about the error codes, see[ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList().then((data: Array<sim.IccAccountInfo>) => {
    console.info(\`getActiveSimAccountInfoList success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getActiveSimAccountInfoList failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getOpKey9+

getOpKey(slotId: number, callback: AsyncCallback<string>): void

Obtains the opkey of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

try {
    sim.getOpKey(0, (err: BusinessError, data: string) => {
    if (err) {
      console.error("getOpKey failed, err: " + JSON.stringify(err));
    } else {
      console.info('getOpKey successfully, data: ' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error("getOpKey err: " + JSON.stringify(err));
}

#### sim.getOpKey9+

getOpKey(slotId: number): Promise<string>

Obtains the opkey of the SIM card in the specified slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOpKey(0).then((data: string) => {
    console.info(\`getOpKey success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getOpKey failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getOpKeySync10+

getOpKeySync(slotId: number): string

Obtains the opkey of the SIM card in the specified slot.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | opkey of the SIM card in the specified slot. |

**Example**

import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpKeySync(0);
console.info(\`getOpKey success, promise: data->${JSON.stringify(data)}\`);

#### sim.getOpName9+

getOpName(slotId: number, callback: AsyncCallback<string>): void

Obtains the OpName of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

try {
    sim.getOpName(0, (err: BusinessError, data: string) => {
    if (err) {
      console.error("getOpName failed, err: " + JSON.stringify(err));
    } else {
      console.info('getOpName successfully, data: ' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error("getOpName err: " + JSON.stringify(err));
}

#### sim.getOpName9+

getOpName(slotId: number): Promise<string>

Obtains the OpName of the SIM card in the specified slot. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOpName(0).then((data: string) => {
    console.info(\`getOpName success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getOpName failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getOpNameSync10+

getOpNameSync(slotId: number): string

Obtains the OpName of the SIM card in the specified slot.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | OpName of the SIM card in the specified slot. |

**Example**

import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpNameSync(0);
console.info(\`getOpName success, promise: data->${JSON.stringify(data)}\`);

#### sim.getDefaultVoiceSimId10+

getDefaultVoiceSimId(callback: AsyncCallback<number>): void

Obtains the default slot ID of the SIM card that provides voice services. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | 
Callback used to return the result.

The return value is bound to the SIM card and increases from 1.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301001 | SIM card is not activated. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSimId((err: BusinessError, data: number) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getDefaultVoiceSimId10+

getDefaultVoiceSimId(): Promise<number>

Obtains the default slot ID of the SIM card that provides voice services. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | 
Promise used to return the result.

The return value is bound to the SIM card and increases from 1.

 |

**Error codes**

For details about the error codes, see[ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301001 | SIM card is not activated. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let promise = sim.getDefaultVoiceSimId();
promise.then((data: number) => {
    console.info(\`getDefaultVoiceSimId success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getDefaultVoiceSimId failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getSimLabel20+

getSimLabel(slotId: number, callback: AsyncCallback<SimLabel>): void

Checks the mapping between card slot IDs and SIM cards.

-   Slot 1 corresponds to SIM card 1 or SIM card 2.
-   Slot 2 corresponds to SIM card 2 or eSIMX.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<[SimLabel](#simlabel20)\> | Yes | Callback used to return the result, which is the SIM card label. |

**Error codes**

For details about the error codes, see [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimLabel(0, (err: BusinessError, data: sim.SimLabel) => {
  console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### sim.getSimLabel20+

getSimLabel(slotId: number): Promise<SimLabel>

Obtains the SIM card label. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SimLabel](#simlabel20) > | Callback used to return the result, which is the SIM card label. |

**Error codes**

For details about the error codes, see [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimLabel(0).then((data: sim.SimLabel) => {
  console.info(\`getSimLabel success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`getSimState failed, promise: err->${JSON.stringify(err)}\`);
});

#### sim.getSimLabelSync20+

getSimLabelSync(slotId: number): SimLabel

Obtains the SIM card label based on the specified SIM card slot ID.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimLabel](#simlabel20) | SIM card label. |

**Example**

import { sim } from '@kit.TelephonyKit';

let simLabel: sim.SimLabel = sim.getSimLabelSync(0);
console.info(\`The sim state is:\` + simLabel);

#### SimType20+

Enumerates the SIM card types.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| PSIM | 0 | Physical SIM card. |
| ESIM | 1 | eSIM card. |

#### SimLabel20+

Defines the SIM card label.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| simType | [SimType](#simtype20) | No | No | SIM card type. |
| index | number | No | No | Unique index ID of the SIM card. |

#### SimState

Enumerates SIM card states.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| SIM\_STATE\_UNKNOWN | 0 | The SIM card is in **unknown** state; that is, the SIM card status cannot be obtained. |
| SIM\_STATE\_NOT\_PRESENT | 1 | The SIM card is in **not present** state; that is, no SIM card is inserted into the card slot. |
| SIM\_STATE\_LOCKED | 2 | The SIM card is in **locked** state; that is, the SIM card is locked by the personal identification number (PIN), PIN unblocking key (PUK), or network. |
| SIM\_STATE\_NOT\_READY | 3 | The SIM card is in **not ready** state; that is, the SIM card has been installed but cannot work properly. |
| SIM\_STATE\_READY | 4 | The SIM card is in **ready** state; that is, the SIM card has been installed and is working properly. |
| SIM\_STATE\_LOADED | 5 | The SIM card is in **loaded** state; that is, the SIM card is present and all its files have been loaded. |

#### CardType7+

Enumerates SIM card types.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN\_CARD | \-1 | Unknown type. |
| SINGLE\_MODE\_SIM\_CARD | 10 | Single-card (SIM). |
| SINGLE\_MODE\_USIM\_CARD | 20 | Single-card (USIM). |
| SINGLE\_MODE\_RUIM\_CARD | 30 | Single-card (RUIM). |
| DUAL\_MODE\_CG\_CARD | 40 | Dual-card (CDMA+GSM). |
| CT\_NATIONAL\_ROAMING\_CARD | 41 | China Telecom internal roaming card. |
| CU\_DUAL\_MODE\_CARD | 42 | China Unicom dual-mode card. |
| DUAL\_MODE\_TELECOM\_LTE\_CARD | 43 | China Telecom dual-mode LTE card. |
| DUAL\_MODE\_UG\_CARD | 50 | Dual-mode card (UMTS+GSM). |
| SINGLE\_MODE\_ISIM\_CARD8+ | 60 | Single-card (ISIM). |

#### IccAccountInfo10+

Defines the ICC account information.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| simId | number | No | No | SIM card ID. |
| slotIndex | number | No | No | Card slot ID. |
| isEsim | boolean | No | No | 
Whether the SIM card is an eSIM.

\- **true**: The SIM card is an eSIM.

\- **false**: The SIM card is not an eSIM.

 |
| isActive | boolean | No | No | 

Whether the card is activated.

**true**: activated.

**false**: not activated.

 |
| iccId | string | No | No | ICCID number. |
| showName | string | No | No | SIM card display name. |
| showNumber | string | No | No | SIM card display number. |
