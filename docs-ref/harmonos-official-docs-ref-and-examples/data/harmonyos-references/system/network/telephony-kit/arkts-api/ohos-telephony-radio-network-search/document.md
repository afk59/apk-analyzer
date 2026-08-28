# @ohos.telephony.radio (Network Search)

The **radio** module provides basic network search management functions. Using the APIs provided by this module, you can obtain the radio access technology (RAT) used in the CS and PS domains, network status, current network selection mode, ISO country code of the registered network, ID of the slot in which the primary card is located, list of signal strengths of the registered network for the SIM card in the specified slot, and carrier name. Besides, you can check whether the current device supports New Radio (NR) and whether the radio service is enabled on the primary SIM card.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/XOjRzXYpR0uah_vYKiOz8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=232BC2FF5E26E86FE7589C1D262D16078BDB8933D6146097EA8D2ABDA0C462AB)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { radio } from '@kit.TelephonyKit';

#### radio.getRadioTech

getRadioTech(slotId: number, callback: AsyncCallback<[NetworkRadioTech](#networkradiotech11)\>): void

Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<[NetworkRadioTech](#networkradiotech11)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getRadioTech(slotId, (err: BusinessError, data: radio.NetworkRadioTech) => {
    if (err) {
        console.error(\`getRadioTech failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getRadioTech success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getRadioTech

getRadioTech(slotId: number): Promise<[NetworkRadioTech](#networkradiotech11)\>

Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

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
| Promise<[NetworkRadioTech](#networkradiotech11)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getRadioTech(slotId).then((data: radio.NetworkRadioTech) => {
    console.info(\`getRadioTech success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getRadioTech failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getRadioTechSync18+

getRadioTechSync(slotId: number): [NetworkRadioTech](#networkradiotech11)

Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

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
| [NetworkRadioTech](#networkradiotech11) | RAT used in the CS and PS domains. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

let slotId: number = 0;
let networkRadioTech: radio.NetworkRadioTech = radio.getRadioTechSync(slotId);
console.info(\`getRadioTechSync success, NetworkRadioTech->${JSON.stringify(networkRadioTech)}\`);

#### radio.getNetworkState

getNetworkState(callback: AsyncCallback<NetworkState>): void

Obtains the network status. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[NetworkState](#networkstate)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

radio.getNetworkState((err: BusinessError, data: radio.NetworkState) => {
    if (err) {
        console.error(\`getNetworkState failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getNetworkState success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getNetworkState

getNetworkState(slotId: number, callback: AsyncCallback<NetworkState>): void

Obtains the network status of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<[NetworkState](#networkstate)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkState(slotId, (err: BusinessError, data: radio.NetworkState) => {
    if (err) {
        console.error(\`getNetworkState failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getNetworkState success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getNetworkState

getNetworkState(slotId?: number): Promise<NetworkState>

Obtains the network status of the SIM card in the specified slot. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | No | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

If no card slot is specified, card slot 1 is used by default.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[NetworkState](#networkstate)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkState(slotId).then((data: radio.NetworkState) => {
    console.info(\`getNetworkState success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getNetworkState failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getNetworkSelectionMode

getNetworkSelectionMode(slotId: number, callback: AsyncCallback<NetworkSelectionMode>): void

Obtains the network selection mode of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<[NetworkSelectionMode](#networkselectionmode)\> | Yes | Callback used to return the result. |

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

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId, (err: BusinessError, data: radio.NetworkSelectionMode) => {
    if (err) {
        console.error(\`getNetworkSelectionMode failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getNetworkSelectionMode success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getNetworkSelectionMode

getNetworkSelectionMode(slotId: number): Promise<NetworkSelectionMode>

Obtains the network selection mode of the SIM card in the specified slot. This API uses a promise to return the result.

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
| Promise<[NetworkSelectionMode](#networkselectionmode)\> | Promise used to return the result. |

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

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId).then((data: radio.NetworkSelectionMode) => {
    console.info(\`getNetworkSelectionMode success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getNetworkSelectionMode failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getISOCountryCodeForNetwork7+

getISOCountryCodeForNetwork(slotId: number, callback: AsyncCallback<string>): void

Obtains the ISO country code of the network with which the SIM card in the specified slot is registered. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. which is a country code, for example, **CN** (China). If the device is not registered with any network, an empty string is returned. |

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

let slotId: number = 0;
radio.getISOCountryCodeForNetwork(slotId, (err: BusinessError, data: string) => {
    if (err) {
        console.error(\`getISOCountryCodeForNetwork failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getISOCountryCodeForNetwork success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getISOCountryCodeForNetwork7+

getISOCountryCodeForNetwork(slotId: number): Promise<string>

Obtains the ISO country code of the network with which the SIM card in the specified slot is registered. This API uses a promise to return the result.

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
| Promise<string> | Promise used to return the result, which is an ISO country code, for example, **CN** (China). If the device is not registered with any network, an empty string is returned. |

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

let slotId: number = 0;
radio.getISOCountryCodeForNetwork(slotId).then((data: string) => {
    console.info(\`getISOCountryCodeForNetwork success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getISOCountryCodeForNetwork failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getISOCountryCodeForNetworkSync10+

getISOCountryCodeForNetworkSync(slotId: number): string

Obtains the ISO country code of the network with which the SIM card in the specified slot is registered.

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
| string | ISO country code of the network, for example, **CN** (China). If the device is not registered with any network, an empty string is returned. |

**Example**

let slotId: number = 0;
let countryISO: string = radio.getISOCountryCodeForNetworkSync(slotId);
console.info(\`the country ISO is:\` + countryISO);

#### radio.getPrimarySlotId7+

getPrimarySlotId(callback: AsyncCallback<number>): void

Obtains the ID of the slot in which the primary card is located. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

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

radio.getPrimarySlotId((err: BusinessError, data: number) => {
    if (err) {
        console.error(\`getPrimarySlotId failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getPrimarySlotId success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getPrimarySlotId7+

getPrimarySlotId(): Promise<number>

Obtains the ID of the slot in which the primary card is located. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see[ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

radio.getPrimarySlotId().then((data: number) => {
    console.info(\`getPrimarySlotId success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getPrimarySlotId failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getSignalInformation7+

getSignalInformation(slotId: number, callback: AsyncCallback<Array<SignalInformation>>): void

Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<Array<[SignalInformation](#signalinformation)\>> | Yes | Callback used to return the result, which is an array of child class objects derived from [SignalInformation](#signalinformation). |

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

let slotId: number = 0;
radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
    if (err) {
        console.error(\`getSignalInformation failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getSignalInformation success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getSignalInformation7+

getSignalInformation(slotId: number): Promise<Array<SignalInformation>>

Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered. This API uses a promise to return the result.

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
| Promise<Array<[SignalInformation](#signalinformation)\>> | Promise used to return the result, which is a list of child class objects derived from [SignalInformation](#signalinformation). |

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

let slotId: number = 0;
radio.getSignalInformation(slotId).then((data: Array<radio.SignalInformation>) => {
    console.info(\`getSignalInformation success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getSignalInformation failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getSignalInformationSync10+

getSignalInformationSync(slotId: number): Array<SignalInformation>

Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered.

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
| Array<[SignalInformation](#signalinformation)\> | Array of child class objects derived from [SignalInformation](#signalinformation). |

**Example**

let slotId: number = 0;
let signalInfo: Array<radio.SignalInformation> = radio.getSignalInformationSync(slotId);
console.info(\`signal information size is:\` + signalInfo.length);

#### radio.isNrSupported8+(deprecated)

isNrSupported(): boolean

Checks whether the current device supports NR.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/VTmOhYkLRTGnx4Q7iwPOig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=285401B815A8D288B297BD7FA588077A697C908E7991CCA0BDBC6D9336C7CFC3)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [isNRSupported](#radioisnrsupported9).

**System capability**: SystemCapability.Telephony.CoreService

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
\- **true**: supported

\- **false**: not supported

 |

**Example**

let result: boolean = radio.isNrSupported();
console.info("Result: "+ result);

#### radio.isNrSupported(deprecated)

isNrSupported(slotId: number): boolean

Checks whether the SIM card in the specified slot supports NR.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/NSi7PQaQScyTo81d6i-bbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7224F619AFB9C15202A8F1BA682508D58467A9AF54E2760E96F9A0B55AB6F39A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isNRSupported](#radioisnrsupported9-1).

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
\- **true**: supported

\- **false**: not supported

 |

**Example**

let slotId: number = 0;
let result: boolean = radio.isNrSupported(slotId);
console.info("Result: "+ result);

#### radio.isNRSupported9+

isNRSupported(): boolean

Checks whether the current device supports NR.

**System capability**: SystemCapability.Telephony.CoreService

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
\- **true**: supported

\- **false**: not supported

 |

**Example**

let result: boolean = radio.isNRSupported();
console.info("Result: "+ result);

#### radio.isNRSupported9+

isNRSupported(slotId: number): boolean

Checks whether the SIM card in the specified slot supports NR.

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
\- **true**: supported

\- **false**: not supported

 |

**Example**

let slotId: number = 0;
let result: boolean = radio.isNRSupported(slotId);
console.info("Result: "+ result);

#### radio.isRadioOn7+

isRadioOn(callback: AsyncCallback<boolean>): void

Checks whether the radio service is enabled on the primary SIM card. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | 
Callback used to return the result.

\- **true**: The radio service is enabled.

\- **false**: The radio service is disabled.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

radio.isRadioOn((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(\`isRadioOn failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`isRadioOn success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.isRadioOn7+

isRadioOn(slotId: number, callback: AsyncCallback<boolean>): void

Checks whether the radio service is enabled on the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

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

\- **true**: The radio service is enabled.

\- **false**: The radio service is disabled.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.isRadioOn(slotId, (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(\`isRadioOn failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`isRadioOn success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.isRadioOn7+

isRadioOn(slotId?: number): Promise<boolean>

Checks whether the radio service is enabled on the SIM card in the specified slot. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | No | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2.

If the slot ID is not specified, this API is defaulted to check whether the radio service is enabled on the primary SIM card.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the result.

\- **true**: The radio service is enabled.

\- **false**: The radio service is disabled.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.isRadioOn(slotId).then((data: boolean) => {
    console.info(\`isRadioOn success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`isRadioOn failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getOperatorName7+

getOperatorName(slotId: number, callback: AsyncCallback<string>): void

Obtains the carrier name of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CoreService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the carrier name, for example, China Mobile. |

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

let slotId: number = 0;
radio.getOperatorName(slotId, (err: BusinessError, data: string) => {
    if (err) {
        console.error(\`getOperatorName failed, callback: err->${JSON.stringify(err)}\`);
        return;
    }
    console.info(\`getOperatorName success, callback: data->${JSON.stringify(data)}\`);
});

#### radio.getOperatorName7+

getOperatorName(slotId: number): Promise<string>

Obtains the carrier name of the SIM card in the specified slot. This API uses a promise to return the result.

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
| Promise<string> | Promise used to return the result, for example, China Mobile. |

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

let slotId: number = 0;
radio.getOperatorName(slotId).then((data: string) => {
    console.info(\`getOperatorName success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getOperatorName failed, promise: err->${JSON.stringify(err)}\`);
});

#### radio.getOperatorNameSync10+

getOperatorNameSync(slotId: number): string

Obtains the carrier name of the SIM card in the specified slot.

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
| string | Carrier name, for example, China Mobile. |

**Example**

let slotId: number = 0;
let operatorName: string = radio.getOperatorNameSync(slotId);
console.info(\`operator name is:\` + operatorName);

#### NetworkRadioTech11+

Defines the radio access technology for the packet switched (PS) or circuit switched (CS) network.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| psRadioTech | [RadioTechnology](#radiotechnology) | No | No | PS. |
| csRadioTech | [RadioTechnology](#radiotechnology) | No | No | CS. |

#### RadioTechnology

Enumerates radio access technologies.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| RADIO\_TECHNOLOGY\_UNKNOWN | 0 | Unknown RAT |
| RADIO\_TECHNOLOGY\_GSM | 1 | Global System for Mobile Communication (GSM) |
| RADIO\_TECHNOLOGY\_1XRTT | 2 | Single-Carrier Radio Transmission Technology (1XRTT) |
| RADIO\_TECHNOLOGY\_WCDMA | 3 | Wideband Code Division Multiple Access (WCDMA) |
| RADIO\_TECHNOLOGY\_HSPA | 4 | High Speed Packet Access (HSPA) |
| RADIO\_TECHNOLOGY\_HSPAP | 5 | Evolved High Speed Packet Access (HSPA+) |
| RADIO\_TECHNOLOGY\_TD\_SCDMA | 6 | TD-SCDMA. |
| RADIO\_TECHNOLOGY\_EVDO | 7 | Evolution-Data Optimized (EVDO) |
| RADIO\_TECHNOLOGY\_EHRPD | 8 | Evolved High Rate Package Data (EHRPD) |
| RADIO\_TECHNOLOGY\_LTE | 9 | Long Term Evolution (LTE) |
| RADIO\_TECHNOLOGY\_LTE\_CA | 10 | Long Term Evolution\_Carrier Aggregation (LTE\_CA) |
| RADIO\_TECHNOLOGY\_IWLAN | 11 | Industrial Wireless LAN (IWLAN) |
| RADIO\_TECHNOLOGY\_NR | 12 | New Radio (NR) |

#### SignalInformation

Defines the signal strength.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| signalType | [NetworkType](#networktype) | No | No | Signal strength type. |
| signalLevel | number | No | No | Signal strength level. |
| dBm9+ | number | No | No | Signal strength, in dBm. |

#### NetworkType

Enumerates network types.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| NETWORK\_TYPE\_UNKNOWN | 0 | Unknown network. |
| NETWORK\_TYPE\_GSM | 1 | GSM network. |
| NETWORK\_TYPE\_CDMA | 2 | CDMA network. |
| NETWORK\_TYPE\_WCDMA | 3 | WCDMA network. |
| NETWORK\_TYPE\_TDSCDMA | 4 | TD-SCDMA network. |
| NETWORK\_TYPE\_LTE | 5 | LTE network. |
| NETWORK\_TYPE\_NR | 6 | NR network. |

#### NetworkState

Defines the network status.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| longOperatorName | string | No | No | Long carrier name of the registered network. |
| shortOperatorName | string | No | No | Short carrier name of the registered network. |
| plmnNumeric | string | No | No | PLMN code of the registered network. |
| isRoaming | boolean | No | No | Whether the user is roaming. |
| regState | [RegState](#regstate) | No | No | Network registration status of the device. |
| cfgTech8+ | [RadioTechnology](#radiotechnology) | No | No | RAT of the device. |
| nsaState | [NsaState](#nsastate) | No | No | NSA network registration status of the device. |
| isCaActive | boolean | No | No | CA status. |
| isEmergency | boolean | No | No | Whether only emergency calls are allowed. |

#### RegState

Defines the network registration status of the device.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| REG\_STATE\_NO\_SERVICE | 0 | The device cannot use any services, including data, SMS, and call services. |
| REG\_STATE\_IN\_SERVICE | 1 | The device can use services properly, including data, SMS, and call services. |
| REG\_STATE\_EMERGENCY\_CALL\_ONLY | 2 | The device can use only the emergency call service. |
| REG\_STATE\_POWER\_OFF | 3 | The device cannot communicate with the network because the cellular radio service is disabled or the modem is powered off. |

#### NsaState

Enumerates NSA network states.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| NSA\_STATE\_NOT\_SUPPORT | 1 | The device is in idle or connected state in an LTE cell that does not support NSA. |
| NSA\_STATE\_NO\_DETECT | 2 | The device is in the idle state in an LTE cell that supports NSA but not NR coverage detection. |
| NSA\_STATE\_CONNECTED\_DETECT | 3 | The device is connected to the LTE network in an LTE cell that supports NSA and NR coverage detection. |
| NSA\_STATE\_IDLE\_DETECT | 4 | The device is in the idle state in an LTE cell that supports NSA and NR coverage detection. |
| NSA\_STATE\_DUAL\_CONNECTED | 5 | The device is connected to the LTE/NR network in an LTE cell that supports NSA. |
| NSA\_STATE\_SA\_ATTACHED | 6 | The device is idle or connected to the NG-RAN cell when being attached to the 5G Core. |

#### NetworkSelectionMode

Enumerates network selection modes.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Value | Description |
| :-- | :-- | :-- |
| NETWORK\_SELECTION\_UNKNOWN | 0 | Unknown network selection mode. |
| NETWORK\_SELECTION\_AUTOMATIC | 1 | Automatic network selection mode. |
| NETWORK\_SELECTION\_MANUAL | 2 | Manual network selection mode. |

#### CellInformation8+

Defines the cell information.

**System capability**: SystemCapability.Telephony.CoreService

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| networkType | [NetworkType](#networktype) | No | No | Network type of the cell. |
| signalInformation | [SignalInformation](#signalinformation) | No | No | Signal information. |
